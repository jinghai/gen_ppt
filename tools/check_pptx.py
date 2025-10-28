#!/usr/bin/env python3
import sys
import zipfile
from pathlib import Path
from lxml import etree as ET

PPTX = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('charts/output/p10-original.pptx')

REQUIRED_PARTS = [
    '_rels/.rels',
    '[Content_Types].xml',
    'docProps/core.xml',
    'docProps/app.xml',
    'ppt/presentation.xml',
    'ppt/_rels/presentation.xml.rels',
    'ppt/slides/slide1.xml',
    'ppt/slides/_rels/slide1.xml.rels',
    'ppt/charts/chart8.xml',
    'ppt/charts/chart9.xml',
    'ppt/charts/_rels/chart8.xml.rels',
    'ppt/charts/_rels/chart9.xml.rels',
    'ppt/theme/theme1.xml',
    'ppt/slideLayouts/slideLayout5.xml',
    'ppt/slideLayouts/_rels/slideLayout5.xml.rels',
    'ppt/slideMasters/slideMaster2.xml',
    'ppt/slideMasters/_rels/slideMaster2.xml.rels',
]

NS_REL = 'http://schemas.openxmlformats.org/package/2006/relationships'
NS_CT = 'http://schemas.openxmlformats.org/package/2006/content-types'


def check_parts(z):
    names = set(z.namelist())
    missing = [p for p in REQUIRED_PARTS if p not in names]
    return names, missing


def check_content_types(z):
    ct = ET.fromstring(z.read('[Content_Types].xml'))
    def has_override(part):
        for o in ct.findall('{%s}Override' % NS_CT):
            if o.get('PartName') == part:
                return True
        return False
    required_overrides = [
        '/ppt/presentation.xml',
        '/ppt/slides/slide1.xml',
        '/ppt/theme/theme1.xml',
        '/docProps/core.xml',
        '/docProps/app.xml',
        '/ppt/charts/chart8.xml',
        '/ppt/charts/chart9.xml',
        '/ppt/slideLayouts/slideLayout5.xml',
        '/ppt/slideMasters/slideMaster2.xml',
    ]
    missing = [p for p in required_overrides if not has_override(p)]
    return missing


def check_slide_rels(z):
    rels = ET.fromstring(z.read('ppt/slides/_rels/slide1.xml.rels'))
    relationships = rels.findall('{%s}Relationship' % NS_REL)
    types = [r.get('Type') for r in relationships]
    targets = [r.get('Target') for r in relationships]
    has_layout = any((t or '').endswith('/slideLayout') for t in types)
    has_chart = any((t or '').endswith('/chart') for t in types)
    has_image = any((t or '').endswith('/image') for t in types)
    charts_rel_ok = any((t or '').endswith('/chart') and (targets[i] or '').startswith('../charts/') for i, t in enumerate(types))
    media_rel_ok = any((targets[i] or '').startswith('../media/') for i in range(len(targets)))
    return {
        'has_layout': has_layout,
        'has_chart': has_chart,
        'has_image': has_image,
        'charts_rel_prefix_ok': charts_rel_ok,
        'media_rel_prefix_ok': media_rel_ok,
        'total_relationships': len(types)
    }


def main():
    if not PPTX.exists():
        print('File not found:', PPTX)
        sys.exit(2)
    with zipfile.ZipFile(PPTX, 'r') as z:
        names, missing = check_parts(z)
        ct_missing = check_content_types(z)
        slide_rels_info = check_slide_rels(z)
    print(f'== {PPTX.name} structure check ==')
    print('Missing parts:', missing or 'None')
    print('Missing content-type overrides:', ct_missing or 'None')
    print('Slide rels:', slide_rels_info)
    # 额外输出：embeddings & media count
    emb = [n for n in names if n.startswith('ppt/embeddings/')]
    media = [n for n in names if n.startswith('ppt/media/')]
    print('Embeddings:', len(emb), emb)
    print('Media:', len(media), media)

if __name__ == '__main__':
    main()