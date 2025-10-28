import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHARTS_ROOT = ROOT / "charts"
INDEX_PATH = CHARTS_ROOT / "output" / "index.json"

README_TMPL = (
    "# p{page} 页面\n\n"
    "该页为批量脚手架占位；当前模板未解压该页 slide。\n"
    "待模板补齐后补充 chartX/fill.py 与 final_data.json，并通过 build_all.py 串联。\n"
)

CONFIG_TMPL = (
    "output:\n  replace_charts: {replace_charts}\n  final_mode: updated\n"
    "fill_policy:\n  keep_original_for_missing: true\n  axis_day_base: 20300\n"
)


def load_index():
    if not INDEX_PATH.exists():
        return {}
    try:
        idx = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        slides = {}
        for s in idx.get("slides", []):
            slide_no = int(s.get("slide"))
            charts = [c.get("name") for c in s.get("charts", []) if c.get("name")]
            slides[slide_no] = charts
        return slides
    except Exception:
        return {}


def scaffold_page(page: int, index: dict):
    page_dir = CHARTS_ROOT / f"p{page}"
    if page_dir.exists():
        print(f"[skip] p{page} exists; leaving intact")
        return
    page_dir.mkdir(parents=True, exist_ok=True)
    charts = index.get(page, [])
    (page_dir / "readme.md").write_text(README_TMPL.format(page=page), encoding="utf-8")
    (page_dir / "config.yaml").write_text(
        CONFIG_TMPL.format(replace_charts=json.dumps(charts, ensure_ascii=False)),
        encoding="utf-8",
    )
    print(f"[scaffold] p{page} created. charts: {charts}")


def main():
    parser = argparse.ArgumentParser(description="Scaffold basic page directories")
    parser.add_argument("pages", nargs="+", type=int, help="Page numbers to scaffold")
    args = parser.parse_args()
    index = load_index()
    for p in args.pages:
        scaffold_page(p, index)

if __name__ == "__main__":
    main()