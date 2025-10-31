#!/usr/bin/env python3
"""
P29页面构建脚本 - 联想法国市场媒体渠道声量份额分析
一键完成数据提取、Excel生成和PPT构建的完整流程
"""
import sys
import atexit
import subprocess
from datetime import datetime
from pathlib import Path

# 文件日志：将输出与错误同步到 logs/build.log
def _init_file_logging():
    """初始化文件日志记录"""
    page_dir = Path(__file__).resolve().parent
    logs_dir = page_dir / 'logs'
    logs_dir.mkdir(parents=True, exist_ok=True)
    fh = open(logs_dir / 'build.log', 'a', encoding='utf-8')
    
    class _Tee:
        def __init__(self, *streams): 
            self.streams = streams
        def write(self, data):
            for s in self.streams:
                try: 
                    s.write(data)
                    s.flush()
                except Exception: 
                    pass
        def flush(self):
            for s in self.streams:
                try: 
                    s.flush()
                except Exception: 
                    pass
    
    sys.stdout = _Tee(sys.__stdout__, fh)
    sys.stderr = _Tee(sys.__stderr__, fh)
    print(f"[log] P29构建开始 {datetime.utcnow().isoformat()}Z")
    
    def _close():
        print(f"[log] P29构建结束 {datetime.utcnow().isoformat()}Z")
        try: 
            fh.flush()
            fh.close()
        except Exception: 
            pass
    atexit.register(_close)

_init_file_logging()

SLIDE_NO = 29
PAGE_DIR = Path(__file__).resolve().parent

def run_generate_excel():
    """步骤1: 运行数据提取和Excel生成脚本"""
    script = PAGE_DIR / 'generate_excel.py'
    if script.exists():
        print(f'[P{SLIDE_NO}] 步骤1: 执行数据提取和Excel生成...')
        try:
            subprocess.run([sys.executable, str(script)], check=True, cwd=str(PAGE_DIR))
            print(f'[P{SLIDE_NO}] ✓ Excel数据文件生成成功')
        except subprocess.CalledProcessError as e:
            print(f'[P{SLIDE_NO}] ✗ Excel生成失败: {e}')
            raise
    else:
        print(f'[P{SLIDE_NO}] ⚠ 跳过Excel生成 (generate_excel.py未找到)')

def run_fill_from_excel():
    """步骤2: 运行PPT填充脚本"""
    script = PAGE_DIR / 'fill_from_excel.py'
    if script.exists():
        print(f'[P{SLIDE_NO}] 步骤2: 执行PPT生成...')
        try:
            subprocess.run([sys.executable, str(script)], check=True, cwd=str(PAGE_DIR))
            print(f'[P{SLIDE_NO}] ✓ PPT文件生成成功')
        except subprocess.CalledProcessError as e:
            print(f'[P{SLIDE_NO}] ✗ PPT生成失败: {e}')
            raise
    else:
        print(f'[P{SLIDE_NO}] ⚠ 跳过PPT生成 (fill_from_excel.py未找到)')

def verify_outputs():
    """步骤3: 验证输出文件"""
    print(f'[P{SLIDE_NO}] 步骤3: 验证输出文件...')
    
    # 检查Excel文件
    excel_file = PAGE_DIR / 'p29_data.xlsx'
    if excel_file.exists():
        size_mb = excel_file.stat().st_size / (1024 * 1024)
        print(f'[P{SLIDE_NO}] ✓ Excel文件: {excel_file.name} ({size_mb:.2f}MB)')
    else:
        print(f'[P{SLIDE_NO}] ✗ Excel文件未找到: {excel_file}')
    
    # 检查PPT文件（在output目录中）
    ppt_file = PAGE_DIR / 'output' / 'p29-final.pptx'
    if ppt_file.exists():
        size_mb = ppt_file.stat().st_size / (1024 * 1024)
        print(f'[P{SLIDE_NO}] ✓ PPT文件: {ppt_file.name} ({size_mb:.2f}MB)')
    else:
        print(f'[P{SLIDE_NO}] ✗ PPT文件未找到: {ppt_file}')

def main():
    """主构建流程"""
    print(f'[P{SLIDE_NO}] ==========================================')
    print(f'[P{SLIDE_NO}] P29页面构建 - 联想法国市场媒体渠道分析')
    print(f'[P{SLIDE_NO}] ==========================================')
    
    try:
        # 步骤1: 生成Excel数据文件
        run_generate_excel()
        
        # 步骤2: 生成PPT文件
        run_fill_from_excel()
        
        # 步骤3: 验证输出文件
        verify_outputs()
        
        print(f'[P{SLIDE_NO}] ==========================================')
        print(f'[P{SLIDE_NO}] ✓ P29页面构建完成!')
        print(f'[P{SLIDE_NO}] 输出文件:')
        print(f'[P{SLIDE_NO}]   - p29_data.xlsx (Excel数据文件)')
        print(f'[P{SLIDE_NO}]   - p29-final.pptx (最终PPT文件)')
        print(f'[P{SLIDE_NO}] ==========================================')
        
    except Exception as e:
        print(f'[P{SLIDE_NO}] ==========================================')
        print(f'[P{SLIDE_NO}] ✗ 构建失败: {e}')
        print(f'[P{SLIDE_NO}] ==========================================')
        sys.exit(1)

if __name__ == '__main__':
    main()
