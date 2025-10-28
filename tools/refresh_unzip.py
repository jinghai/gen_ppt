#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 gen_ppt/config.yaml 读取 original_ppt 与 template_root，
将 PPTX 解压覆盖到 template_root（不清空，按文件覆盖），
用于修复解压目录与当前模板不一致导致的校验误差。

使用示例：
  python3 gen_ppt/tools/refresh_unzip.py
  python3 gen_ppt/tools/refresh_unzip.py --ppt input/LRTBH.pptx --out-root input/LRTBH-unzip
"""
from __future__ import annotations
import argparse
import json
import zipfile
from pathlib import Path
from typing import Dict, List
import shutil

import yaml


def _find_root(start: Path) -> Path:
    p = start
    while p.parent != p:
        if (p / 'config.yaml').exists() and (p / 'input').exists():
            return p
        p = p.parent
    return start

TOOLS_DIR = Path(__file__).resolve().parent
ROOT = _find_root(TOOLS_DIR)
CFG = ROOT / 'config.yaml'


def _load_cfg() -> Dict:
    try:
        return yaml.safe_load(CFG.read_text(encoding='utf-8')) or {}
    except Exception:
        return {}


def _resolve_paths(pptx_arg: str | None, out_root_arg: str | None) -> tuple[Path, Path]:
    cfg = _load_cfg()
    prj = cfg.get('project') or {}
    pptx = Path(pptx_arg) if pptx_arg else Path(prj.get('original_ppt', 'input/LRTBH.pptx'))
    if not pptx.is_absolute():
        pptx = ROOT / pptx
    out_root = Path(out_root_arg) if out_root_arg else Path(prj.get('template_root', 'input/LRTBH-unzip'))
    if not out_root.is_absolute():
        out_root = ROOT / out_root
    return pptx, out_root


def refresh_unzip(pptx_path: Path, out_root: Path) -> dict:
    out_root.mkdir(parents=True, exist_ok=True)
    written = 0
    with zipfile.ZipFile(pptx_path, 'r') as z:
        for name in z.namelist():
            # 仅写出文件，目录跳过；保持 zip 内路径层级（ppt/...）
            if name.endswith('/'):
                continue
            dest = out_root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            data = z.read(name)
            dest.write_bytes(data)
            written += 1
    return {'pptx': str(pptx_path), 'out_root': str(out_root), 'files_written': written}


def prune_legacy(out_root: Path) -> dict:
    """删除 out_root 下顶层的旧版镜像目录（非 ppt/ 层级）。
    仅删除根下的以下目录名称：charts, slides, media, embeddings, diagrams, drawings,
    notesSlides, notesMasters, slideMasters, slideLayouts, theme。
    """
    legacy_names: List[str] = [
        'charts', 'slides', 'media', 'embeddings', 'diagrams', 'drawings',
        'notesSlides', 'notesMasters', 'slideMasters', 'slideLayouts', 'theme',
    ]
    removed: List[str] = []
    for name in legacy_names:
        target = out_root / name
        # 只处理顶层，避免误删 ppt/ 下的同名目录
        if target.exists() and target.is_dir():
            shutil.rmtree(target)
            removed.append(str(target))
    return {'removed_count': len(removed), 'removed': removed}


def main():
    ap = argparse.ArgumentParser(description='刷新模板解压目录（从 PPTX 解压覆盖）')
    ap.add_argument('--ppt', dest='pptx', help='PPTX 文件路径，默认取 config.yaml.project.original_ppt')
    ap.add_argument('--out-root', dest='out_root', help='解压输出根目录，默认取 config.yaml.project.template_root')
    ap.add_argument('--report', dest='report', default=str(ROOT / 'output' / 'refresh_unzip.json'), help='输出报告 JSON 路径')
    ap.add_argument('--prune-legacy', dest='prune_legacy', action='store_true', help='清理解压根目录下顶层旧镜像（charts、slides 等非 ppt/ 层级）')
    args = ap.parse_args()

    pptx_path, out_root = _resolve_paths(args.pptx, args.out_root)
    if not pptx_path.exists():
        raise SystemExit(f'PPTX not found: {pptx_path}')
    summary = refresh_unzip(pptx_path, out_root)
    if args.prune_legacy:
        summary['prune_legacy'] = prune_legacy(out_root)
    # 写出报告
    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False))
    print('written report:', report_path)


if __name__ == '__main__':
    main()