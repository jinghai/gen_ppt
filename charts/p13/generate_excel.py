#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
P13 页面：Engagement breakdown 数据生成脚本

职责：
- 读取页面级配置 config.yaml（仅引用本页配置，不依赖全局配置）；
- 从 Neticle 宽表中按国家与关键词过滤数据，计算：
  - 情绪分类（Positive/Neutral/Negative）与月度占比（用于饼图）；
  - 每日情绪占比折线数据（Positive/Neutral/Negative）；
  - Engagement（参与度）按天聚合与月度汇总：
    total_engagement = 候选互动字段求和；
    ipm = total_engagement / impressions * 1000（无曝光时置为 None）。
- 将结果写入同一个 Excel：PieData、LineData、MetaData 三个工作表。

备注：
- 尽量使用宽表。为兼容不同名称，自动探测 mentions_wide 表与可用字段；
- 不打开大库做手动检查，运行时只按过滤条件读取必要列；
- 所有临时文件放置在页面级 tmp 目录。
"""

import os
import sys
import json
import math
import sqlite3
import datetime as dt
from typing import Dict, List, Tuple, Optional

try:
    import yaml
except Exception as e:
    print("缺少依赖：pyyaml。请安装后重试。")
    raise

try:
    from openpyxl import Workbook
except Exception:
    print("缺少依赖：openpyxl。请安装后重试。")
    raise


class P13DataGenerator:
    def __init__(self, config_path: str):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.cfg = yaml.safe_load(f)

        self.page_root = os.path.dirname(os.path.abspath(config_path))
        self.project = self.cfg.get('project', {})
        self.data_sources = self.cfg.get('data_sources', {})
        self.time_range = self.cfg.get('time_range', {})
        self.filters = self.cfg.get('filters', {})
        self.sentiment = self.cfg.get('sentiment', {})
        self.charts = self.cfg.get('charts', {})
        self.engagement_cfg = self.cfg.get('engagement', {})
        self.output_cfg = self.cfg.get('output', {})
        self.fill_policy = self.cfg.get('fill_policy', {})
        self.logging_cfg = self.cfg.get('logging', {})

        # 路径
        self.tmp_dir = os.path.join(self.page_root, self.project.get('tmp_dir', 'tmp'))
        self.output_dir = os.path.join(self.page_root, self.project.get('output_dir', 'output'))
        self.excel_file_name = self.output_cfg.get('excel_file_name', 'p13_data.xlsx')
        self.excel_file_path = os.path.join(self.output_dir, self.excel_file_name)

        # 颜色与阈值
        self.labels = self.sentiment.get('labels', ['Positive', 'Neutral', 'Negative'])
        thresholds = self.sentiment.get('thresholds', {})
        self.pos_min = float(thresholds.get('positive_min', 0.05))
        self.neg_max = float(thresholds.get('negative_max', -0.05))

        # Engagement 字段候选
        self.eng_fields_candidates: List[str] = self.engagement_cfg.get('fields_candidates', [])
        self.impr_fields_candidates: List[str] = self.engagement_cfg.get('impressions_fields', [])

        # 运行时信息
        self.wide_table_name: Optional[str] = None
        self.wide_columns: List[str] = []

    # ---------- 基础工具 ----------
    def _ensure_dirs(self):
        os.makedirs(self.tmp_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def _to_date(self, s) -> dt.date:
        """将配置中的日期值统一为 date。
        - 支持 `datetime.date`/`datetime.datetime` 直接返回/取 date；
        - 支持字符串格式 `YYYY-MM-DD`；
        - 其余情况抛出 TypeError 以便尽早暴露配置问题。
        """
        if s is None:
            raise TypeError('start_date/end_date 未设置')
        if isinstance(s, dt.date):
            return s
        if isinstance(s, dt.datetime):
            return s.date()
        if isinstance(s, str):
            return dt.datetime.strptime(s.strip(), '%Y-%m-%d').date()
        raise TypeError(f'不支持的日期类型: {type(s)}')

    def _day_range(self) -> List[dt.date]:
        start = self._to_date(self.time_range.get('start_date'))
        end = self._to_date(self.time_range.get('end_date'))
        days = []
        cur = start
        while cur <= end:
            days.append(cur)
            cur += dt.timedelta(days=1)
        return days

    def _date_to_utc_ms_bounds(self, d: dt.date) -> Tuple[int, int]:
        start_dt = dt.datetime(d.year, d.month, d.day, 0, 0, 0)
        end_dt = start_dt + dt.timedelta(days=1) - dt.timedelta(milliseconds=1)
        epoch = dt.datetime(1970, 1, 1)
        start_ms = int((start_dt - epoch).total_seconds() * 1000)
        end_ms = int((end_dt - epoch).total_seconds() * 1000)
        return start_ms, end_ms

    # ---------- 数据库探测 ----------
    def _connect_neticle(self) -> sqlite3.Connection:
        db_path = os.path.join(self.page_root, self.data_sources.get('neticle_db'))
        if not os.path.isabs(db_path):
            db_path = os.path.abspath(db_path)
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"未找到 Neticle DB: {db_path}")
        return sqlite3.connect(db_path)

    def _detect_wide_table(self, con: sqlite3.Connection) -> str:
        cur = con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        names = [r[0] for r in cur.fetchall()]
        candidates = [n for n in names if 'mentions_wide' in n.lower()]
        if not candidates:
            raise RuntimeError("未找到 mentions_wide 表，请检查数据库结构或更新配置。")
        # 优先 neticle_mentions_wide
        for n in candidates:
            if 'neticle' in n.lower():
                return n
        return candidates[0]

    def _load_columns(self, con: sqlite3.Connection, table: str) -> List[str]:
        cur = con.cursor()
        cur.execute(f"PRAGMA table_info('{table}')")
        cols = [r[1] for r in cur.fetchall()]
        return cols

    # ---------- 动态构造查询 ----------
    def _pick_first_existing(self, candidates: List[str]) -> Optional[str]:
        for c in candidates:
            if c in self.wide_columns:
                return c
        return None

    def _build_where(self) -> Tuple[str, List]:
        params: List = []

        # 国家过滤字段候选
        country_col = self._pick_first_existing(['countryId', 'country_id', 'country'])
        where_clauses = []
        if country_col:
            where_clauses.append(f"{country_col} = ?")
            params.append(int(self.filters.get('country_id')))

        # 关键词过滤（品牌）字段候选
        keyword_col = self._pick_first_existing(['keyword', 'keyword_label', 'keywordLabel'])
        if keyword_col and self.filters.get('keyword_like'):
            where_clauses.append(f"{keyword_col} LIKE ?")
            params.append(self.filters.get('keyword_like'))

        # 时间范围
        created_col = self._pick_first_existing(['createdAtUtcMs', 'createdAtMs', 'createdAt'])
        if created_col:
            # 整体区间过滤，减少 IO
            start_d = self._to_date(self.time_range.get('start_date'))
            end_d = self._to_date(self.time_range.get('end_date'))
            epoch = dt.datetime(1970, 1, 1)
            start_ms = int((dt.datetime.combine(start_d, dt.time.min) - epoch).total_seconds() * 1000)
            end_ms = int((dt.datetime.combine(end_d, dt.time.max) - epoch).total_seconds() * 1000)
            where_clauses.append(f"{created_col} BETWEEN ? AND ?")
            params.extend([start_ms, end_ms])

        where_sql = ''
        if where_clauses:
            where_sql = 'WHERE ' + ' AND '.join(where_clauses)
        return where_sql, params

    def _select_columns(self) -> List[str]:
        cols = []
        # 必要列
        for c in ['polarity', 'createdAtUtcMs', 'createdAtMs', 'createdAt']:
            if c in self.wide_columns:
                cols.append(c)

        # Engagement 候选列（存在才加入）
        for c in self.eng_fields_candidates:
            if c in self.wide_columns:
                cols.append(c)

        # 曝光候选列
        for c in self.impr_fields_candidates:
            if c in self.wide_columns:
                cols.append(c)

        # 国家与关键词列（便于调试与后续校验）
        for c in ['countryId', 'country_id', 'country', 'keyword', 'keyword_label', 'keywordLabel']:
            if c in self.wide_columns:
                cols.append(c)

        # 去重保持顺序
        dedup = []
        seen = set()
        for c in cols:
            if c not in seen:
                dedup.append(c)
                seen.add(c)
        return dedup

    # ---------- 计算逻辑 ----------
    def _classify_sentiment(self, polarity: Optional[float]) -> str:
        if polarity is None:
            return 'Neutral'
        try:
            p = float(polarity)
        except Exception:
            return 'Neutral'
        if p > self.pos_min:
            return 'Positive'
        if p < self.neg_max:
            return 'Negative'
        return 'Neutral'

    def _calc_row_engagement(self, row: Dict[str, Optional[float]]) -> Tuple[float, Optional[float]]:
        # total_engagement
        total = 0.0
        for c in self.eng_fields_candidates:
            v = row.get(c)
            if v is None:
                continue
            try:
                total += float(v)
            except Exception:
                continue

        # impressions
        impressions = 0.0
        found_impr = False
        for c in self.impr_fields_candidates:
            v = row.get(c)
            if v is None:
                continue
            try:
                impressions += float(v)
                found_impr = True
            except Exception:
                continue

        ipm = None
        if found_impr and impressions > 0:
            ipm = (total / impressions) * 1000.0
        return total, ipm

    def _pick_created_ms(self, row: Dict) -> Optional[int]:
        for c in ['createdAtUtcMs', 'createdAtMs', 'createdAt']:
            v = row.get(c)
            if v is None:
                continue
            try:
                return int(v)
            except Exception:
                pass
        return None

    def _ms_to_date(self, ms: int) -> dt.date:
        return dt.datetime.utcfromtimestamp(ms / 1000.0).date()

    # ---------- 主流程 ----------
    def run(self) -> None:
        self._ensure_dirs()

        # 探测表和字段
        con = self._connect_neticle()
        try:
            self.wide_table_name = self._detect_wide_table(con)
            self.wide_columns = self._load_columns(con, self.wide_table_name)

            where_sql, params = self._build_where()
            select_cols = self._select_columns()
            if not select_cols:
                raise RuntimeError("没有可选取的列，无法生成数据。")

            sql = f"SELECT {', '.join(select_cols)} FROM {self.wide_table_name} {where_sql}"
            cur = con.cursor()
            cur.execute(sql, params)

            # 聚合容器
            pie_counts = {lbl: 0 for lbl in self.labels}
            day_buckets: Dict[dt.date, Dict[str, float]] = {}
            day_eng_total: Dict[dt.date, float] = {}
            day_impr_total: Dict[dt.date, float] = {}

            for row_t in cur.fetchall():
                row = {select_cols[i]: row_t[i] for i in range(len(select_cols))}

                # 时间
                ms = self._pick_created_ms(row)
                if ms is None:
                    continue
                d = self._ms_to_date(ms)

                # 过滤到配置区间（保险）
                start_d = self._to_date(self.time_range.get('start_date'))
                end_d = self._to_date(self.time_range.get('end_date'))
                if not (start_d <= d <= end_d):
                    continue

                # 情绪分类
                sentiment = self._classify_sentiment(row.get('polarity'))
                pie_counts[sentiment] = pie_counts.get(sentiment, 0) + 1
                if d not in day_buckets:
                    day_buckets[d] = {lbl: 0.0 for lbl in self.labels}
                day_buckets[d][sentiment] += 1.0

                # Engagement
                total, ipm_row = self._calc_row_engagement(row)
                day_eng_total[d] = day_eng_total.get(d, 0.0) + total
                # impressions 聚合为总和（若存在）
                # 这里复用 _calc_row_engagement 内部 impressions 计算逻辑
                impressions_row = 0.0
                for c in self.impr_fields_candidates:
                    v = row.get(c)
                    if v is None:
                        continue
                    try:
                        impressions_row += float(v)
                    except Exception:
                        continue
                day_impr_total[d] = day_impr_total.get(d, 0.0) + impressions_row

        finally:
            con.close()

        # 生成 Excel
        wb = Workbook()
        ws_pie = wb.active
        ws_pie.title = self.charts.get('pie', {}).get('sheet_name', 'PieData')
        ws_line = wb.create_sheet(self.charts.get('line', {}).get('sheet_name', 'LineData'))
        ws_meta = wb.create_sheet('MetaData')

        # PieData：按月度总量计算百分比
        total_mentions = sum(pie_counts.values())
        ws_pie.append(['Sentiment', 'Percentage'])
        for lbl in self.labels:
            count = pie_counts.get(lbl, 0)
            pct = (count / total_mentions * 100.0) if total_mentions > 0 else 0.0
            ws_pie.append([lbl, round(pct, 2)])

        # LineData：每日情绪百分比 + Engagement 附加列（便于校验）
        ws_line.append(['Date', 'Positive', 'Neutral', 'Negative', 'EngagementTotal', 'Impressions', 'IPM'])
        for d in sorted(day_buckets.keys()):
            bucket = day_buckets[d]
            day_total = sum(bucket.values())
            pos = (bucket.get('Positive', 0.0) / day_total * 100.0) if day_total > 0 else 0.0
            neu = (bucket.get('Neutral', 0.0) / day_total * 100.0) if day_total > 0 else 0.0
            neg = (bucket.get('Negative', 0.0) / day_total * 100.0) if day_total > 0 else 0.0

            eng_total = day_eng_total.get(d, 0.0)
            impr_total = day_impr_total.get(d, 0.0)
            ipm = (eng_total / impr_total * 1000.0) if impr_total and impr_total > 0 else None

            ws_line.append([
                d.strftime('%Y-%m-%d'),
                round(pos, 2),
                round(neu, 2),
                round(neg, 2),
                round(eng_total, 2),
                round(impr_total, 2),
                round(ipm, 2) if ipm is not None else None,
            ])

        # MetaData：写入基础信息
        meta_pairs = [
            ('Page', self.project.get('page')), 
            ('Country', self.filters.get('country_name')), 
            ('CountryId', self.filters.get('country_id')), 
            ('BrandKey', self.filters.get('brand_key')), 
            ('KeywordLike', self.filters.get('keyword_like')), 
            ('StartDate', self.time_range.get('start_date')), 
            ('EndDate', self.time_range.get('end_date')), 
            ('TotalMentions', total_mentions),
        ]
        ws_meta.append(['Key', 'Value'])
        for k, v in meta_pairs:
            ws_meta.append([k, v])

        # 保存 Excel
        wb.save(self.excel_file_path)
        print(f"数据已生成：{self.excel_file_path}")


def main():
    page_dir = os.path.dirname(os.path.abspath(__file__))
    cfg_path = os.path.join(page_dir, 'config.yaml')
    gen = P13DataGenerator(cfg_path)
    gen.run()


if __name__ == '__main__':
    main()