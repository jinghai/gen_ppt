"""
构建原始 PPT（仅本页），基于页面微模板。

策略与约束（MVP，避免过度设计）：
- 只使用页面 `template/` 目录下的微模板，不做 UNZ 回退或跨页面依赖。
- 严格校验 `ppt/embeddings` 中的嵌入数据类型，仅允许 `.xlsb`。
- 需要存在关键文件：`slide1.xml`、`presentation.xml(.rels)`、`[Content_Types].xml`、`ppt/charts/_rels/`。
- 输出日志到当前页面 `logs/build_original.log`，并在控制台同步打印。
- 直接将微模板目录打包为 `pXX-original.pptx`（XX 为页码），不进行冗余的 XML 过滤（微模板已是单页）。

该实现兼顾可读性与稳健性，满足当前需求并便于后续扩展。
"""

from __future__ import annotations

import zipfile
from datetime import datetime
from pathlib import Path


def _page_dir() -> Path:
    return Path(__file__).resolve().parent


def _slide_no_from_dir(page_dir: Path) -> int:
    name = page_dir.name
    if not name.startswith('p'):
        raise ValueError(f'Invalid page dir name: {name}')
    return int(name[1:])


PAGE_DIR = _page_dir()
SLIDE_NO = _slide_no_from_dir(PAGE_DIR)
TEMPLATE_DIR = PAGE_DIR / 'template'
EMBED_DIR = TEMPLATE_DIR / 'ppt' / 'embeddings'
SLIDES_DIR = TEMPLATE_DIR / 'ppt' / 'slides'
PRES_DIR = TEMPLATE_DIR / 'ppt'
CHARTS_DIR = TEMPLATE_DIR / 'ppt' / 'charts'
CHARTS_RELS_DIR = CHARTS_DIR / '_rels'

OUT_PPTX = PAGE_DIR / 'output' / f'p{SLIDE_NO}-original.pptx'
LOG_DIR = PAGE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'build_original.log'


def log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    line = f'[{ts}] [p{SLIDE_NO}] {msg}'
    print(line)
    with LOG_FILE.open('a', encoding='utf-8') as f:
        f.write(line + '\n')


def assert_micro_template_integrity() -> None:
    """校验微模板的关键结构与约束。"""
    if not TEMPLATE_DIR.exists():
        raise FileNotFoundError(f'Micro template missing: {TEMPLATE_DIR}')

    required_files = [
        SLIDES_DIR / 'slide1.xml',
        PRES_DIR / 'presentation.xml',
        PRES_DIR / '_rels' / 'presentation.xml.rels',
        TEMPLATE_DIR / '[Content_Types].xml',
    ]
    for p in required_files:
        if not p.exists():
            raise FileNotFoundError(f'Required file missing: {p}')

    if not EMBED_DIR.exists():
        raise FileNotFoundError(f'Embeddings directory missing: {EMBED_DIR}')
    bad = [p for p in EMBED_DIR.iterdir() if p.is_file() and p.suffix.lower() != '.xlsb']
    if bad:
        raise ValueError(f'Only .xlsb allowed in embeddings, found: {", ".join(b.name for b in bad)}')

    if not CHARTS_RELS_DIR.exists():
        raise FileNotFoundError(f'Charts rels directory missing: {CHARTS_RELS_DIR}')


def build() -> None:
    """将微模板完整打包为原始 PPTX（单页）。"""
    log('Start build_original')
    assert_micro_template_integrity()
    OUT_PPTX.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(OUT_PPTX, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(TEMPLATE_DIR.rglob('*')):
            if p.is_file():
                arc = p.relative_to(TEMPLATE_DIR)
                z.write(p, arcname=str(arc))
    log(f'Wrote {OUT_PPTX}')


def main() -> None:
    try:
        build()
    except Exception as e:
        log(f'ERROR: {e!r}')
        raise


if __name__ == '__main__':
    main()