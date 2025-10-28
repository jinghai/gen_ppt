#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复 charts/charts/p8..p31 子集的缺失资产：
- 确保 chart_path.txt 指向解压目录的 XML；必要时补充缺失的 chart 目录与 fill.py（不覆盖现有）
- 针对缺数据的页面运行 make_data.py 生成 data.json 与 final_data.json
- 生成缺失的 original_* 原始缓存（类型感知）
- 离线生成缺失的 preview_original.png 预览图
- 最后输出修复摘要

注意：不进行任何 HTTP 预览或下载操作
"""
from __future__ import annotations
import argparse
import json
import subprocess
from pathlib import Path
from typing import Dict, List

import yaml

REPO = Path(__file__).resolve().parents[1]
PAGES_ROOT = REPO / 'charts'
AUDIT_JSON = REPO / 'output' / 'audit_subset.json'
TOOLS_DIR = REPO / 'tools'

def _resolve_unz_root() -> Path:
    """从 config.yaml 解析模板解压根目录，默认回退到 input/LRTBH-unzip。
    支持两种结构：顶层 charts/ 与嵌套 ppt/charts/。
    """
    cfg_path = REPO / 'config.yaml'
    try:
        cfg = yaml.safe_load(cfg_path.read_text(encoding='utf-8')) or {}
    except Exception:
        cfg = {}
    tr = (cfg.get('project') or {}).get('template_root', 'input/LRTBH-unzip')
    p = Path(tr)
    if not p.is_absolute():
        p = REPO / tr
    return p

def _charts_dir(unz: Path) -> Path:
    d = unz / 'ppt' / 'charts'
    return d if d.exists() else unz / 'charts'

# 简化版填充脚本模板：仅在缺失时创建占位，不覆盖已有 fill.py
FILL_TEMPLATE = (
    "#!/usr/bin/env python3\n"
    "print('[info] filler stub: implement chart fill after data is ready')\n"
)


def ensure_chart_paths_and_fillers(pages: List[str], summary: Dict[str, object]):
    charts_root = _charts_dir(_resolve_unz_root())
    for pname in pages:
        pdir = PAGES_ROOT / pname
        cfg = pdir / 'config.yaml'
        if not cfg.exists():
            continue
        try:
            data = yaml.safe_load(cfg.read_text(encoding='utf-8')) or {}
        except Exception:
            data = {}
        charts = (data.get('output') or {}).get('replace_charts') or []
        for ch in charts:
            # ch 形如 chart8.xml
            chart_id = ch.replace('.xml','')
            cdir = pdir / chart_id
            cdir.mkdir(parents=True, exist_ok=True)
            chart_xml = charts_root / ch
            # chart_path.txt 写入绝对路径，避免 cwd 影响
            chart_path = cdir / 'chart_path.txt'
            need_write = (not chart_path.exists())
            current = chart_path.read_text(encoding='utf-8').strip() if chart_path.exists() else ''
            if not current or not Path(current).exists():
                need_write = True
            if need_write:
                chart_path.write_text(str(chart_xml), encoding='utf-8')
                (summary.setdefault('chart_paths_written', [])).append(str(chart_path))
            # 如缺少 fill.py 则补充模板，不覆盖已有
            filler = cdir / 'fill.py'
            if not filler.exists():
                filler.write_text(FILL_TEMPLATE, encoding='utf-8')
                (summary.setdefault('fillers_created', [])).append(str(filler))


def run_make_data_for_missing_pages(pages: List[str], summary: Dict[str, object]):
    missing_pages: List[str] = []
    if AUDIT_JSON.exists():
        try:
            audit = json.loads(AUDIT_JSON.read_text(encoding='utf-8'))
            for page in audit.get('pages', []):
                pname = page.get('page')
                if pname not in pages:
                    continue
                # 如果该页面的任何图表缺 data.json 或 final_data.json，则触发运行
                any_missing_data = False
                for ch in page.get('charts', []):
                    miss = ch.get('missing') or []
                    if 'data.json' in miss or 'final_data.json' in miss:
                        any_missing_data = True
                        break
                if any_missing_data:
                    missing_pages.append(pname)
        except Exception:
            pass
    for pname in sorted(set(missing_pages)):
        pdir = PAGES_ROOT / pname
        mpy = pdir / 'make_data.py'
        if mpy.exists():
            try:
                subprocess.run(['python3', str(mpy)], cwd=str(REPO), check=False)
                (summary.setdefault('pages_make_data_run', [])).append(pname)
            except Exception:
                pass


def run_original_cache_generation(pages: List[str], summary: Dict[str, object]):
    try:
        subprocess.run([
            'python3', str(TOOLS_DIR / 'generate_original_cache.py'),
            '--pages', *pages,
            '--out-json', str(REPO / 'charts' / 'output' / 'original_cache_subset_summary.json')
        ], cwd=str(REPO), check=False)
        summary['original_cache_run'] = True
    except Exception:
        summary['original_cache_run'] = False


def run_offline_previews(summary: Dict[str, object]):
    try:
        subprocess.run(['python3', str(TOOLS_DIR / 'gen_preview_all.py')], cwd=str(REPO), check=False)
        summary['previews_run'] = True
    except Exception:
        summary['previews_run'] = False


def main():
    ap = argparse.ArgumentParser(description='批量修复缺失资产（子集 p8..p31）')
    ap.add_argument('--pages', nargs='*', default=[
        'p8','p10','p12','p13','p14','p15','p16','p17','p18','p19','p21','p22','p23','p24','p25','p26','p27','p29','p30','p31'
    ], help='要处理的页面目录名')
    args = ap.parse_args()

    pages: List[str] = args.pages
    summary: Dict[str, object] = {
        'pages': pages,
        'chart_paths_written': [],
        'fillers_created': [],
        'pages_make_data_run': [],
        'original_cache_run': False,
        'previews_run': False,
    }

    ensure_chart_paths_and_fillers(pages, summary)
    run_make_data_for_missing_pages(pages, summary)
    run_original_cache_generation(pages, summary)
    run_offline_previews(summary)

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()