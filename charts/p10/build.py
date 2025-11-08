#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
P10 构建脚本 - 一键完成从数据提取到PPT生成的完整流程
整合执行generate_excel.py和fill_from_excel.py，方便一键完成构建任务
"""

import os
import sys
import subprocess
import yaml
import logging
import time
from pathlib import Path
from datetime import datetime

class P10Builder:
    """P10页面构建器"""
    
    def __init__(self, config_path="config.yaml"):
        """初始化构建器"""
        self.config_path = config_path
        self.config = self._load_config()
        self._setup_logging()
        self.logger = logging.getLogger(__name__)
        
        # 设置脚本路径
        self.script_dir = Path(__file__).parent
        self.generate_script = self.script_dir / "generate_excel.py"
        self.fill_script = self.script_dir / "fill_from_excel.py"
        
    def _load_config(self):
        """加载页面级配置文件"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"错误：无法加载配置文件 {self.config_path}: {e}")
            sys.exit(1)
            
    def _setup_logging(self):
        """设置日志配置"""
        log_config = self.config.get('logging', {})
        
        # 创建logs目录
        logs_dir = Path(__file__).parent / 'logs'
        logs_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=getattr(logging, log_config.get('level', 'INFO')),
            format=log_config.get('format', '%(asctime)s - %(levelname)s - %(message)s'),
            handlers=[
                logging.FileHandler(logs_dir / 'build.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        
    def _check_prerequisites(self):
        """检查构建前提条件"""
        self.logger.info("检查构建前提条件...")
        
        errors = []
        
        # 检查脚本文件
        if not self.generate_script.exists():
            errors.append(f"数据生成脚本不存在: {self.generate_script}")
            
        if not self.fill_script.exists():
            errors.append(f"PPT填充脚本不存在: {self.fill_script}")
            
        # 检查配置文件
        if not Path(self.config_path).exists():
            errors.append(f"配置文件不存在: {self.config_path}")
            
        # 检查数据源
        data_sources = self.config.get('data_sources', {})
        for db_name, db_path in data_sources.items():
            if not Path(db_path).exists():
                errors.append(f"数据库文件不存在: {db_path} ({db_name})")
                
        # 检查PPT模板
        template_file = Path(self.config['project']['template_file'])
        if not template_file.exists():
            errors.append(f"PPT模板文件不存在: {template_file}")
            
        if errors:
            for error in errors:
                self.logger.error(error)
            raise RuntimeError("构建前提条件检查失败")
            
        self.logger.info("✅ 构建前提条件检查通过")
        
    def _run_script(self, script_path, description):
        """运行Python脚本"""
        self.logger.info(f"开始执行: {description}")
        start_time = time.time()
        
        try:
            # 使用当前Python解释器运行脚本
            result = subprocess.run(
                [sys.executable, str(script_path)],
                cwd=self.script_dir,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            elapsed_time = time.time() - start_time
            
            if result.returncode == 0:
                self.logger.info(f"✅ {description} 执行成功 (耗时: {elapsed_time:.2f}秒)")
                if result.stdout.strip():
                    self.logger.info(f"输出: {result.stdout.strip()}")
                return True
            else:
                self.logger.error(f"❌ {description} 执行失败 (返回码: {result.returncode})")
                if result.stderr.strip():
                    self.logger.error(f"错误输出: {result.stderr.strip()}")
                if result.stdout.strip():
                    self.logger.error(f"标准输出: {result.stdout.strip()}")
                return False
                
        except Exception as e:
            elapsed_time = time.time() - start_time
            self.logger.error(f"❌ {description} 执行异常 (耗时: {elapsed_time:.2f}秒): {e}")
            return False
            
    def _validate_outputs(self):
        """验证输出文件"""
        self.logger.info("验证输出文件...")
        
        # 检查Excel文件
        excel_file = Path(self.config['output']['excel_file'])
        if not excel_file.exists():
            self.logger.error(f"Excel文件未生成: {excel_file}")
            return False
            
        # 检查最终PPT文件
        output_dir = Path(self.config['project']['output_dir'])
        final_ppt = output_dir / self.config['output']['final_ppt']
        if not final_ppt.exists():
            self.logger.error(f"最终PPT文件未生成: {final_ppt}")
            return False
            
        # 检查文件大小
        excel_size = excel_file.stat().st_size
        ppt_size = final_ppt.stat().st_size
        
        if excel_size == 0:
            self.logger.error("Excel文件为空")
            return False
            
        if ppt_size == 0:
            self.logger.error("PPT文件为空")
            return False
            
        self.logger.info(f"✅ 输出文件验证通过:")
        self.logger.info(f"  - Excel文件: {excel_file} ({excel_size:,} bytes)")
        self.logger.info(f"  - PPT文件: {final_ppt} ({ppt_size:,} bytes)")
        
        return True
        
    def run(self):
        """执行完整的构建流程"""
        start_time = time.time()
        
        try:
            self.logger.info("=" * 60)
            self.logger.info("🚀 P10 页面构建开始")
            self.logger.info("=" * 60)
            
            # 1. 检查前提条件
            self._check_prerequisites()
            
            # 2. 执行数据生成
            if not self._run_script(self.generate_script, "数据生成 (generate_excel.py)"):
                raise RuntimeError("数据生成失败")
                
            # 3. 执行PPT填充
            if not self._run_script(self.fill_script, "PPT填充 (fill_from_excel.py)"):
                raise RuntimeError("PPT填充失败")
                
            # 4. 验证输出文件
            if not self._validate_outputs():
                raise RuntimeError("输出文件验证失败")
                
            end_time = time.time()
            duration = end_time - start_time
            
            self.logger.info("=" * 60)
            self.logger.info(f"🎉 P10 页面构建成功完成! (耗时: {duration:.2f}秒)")
            self.logger.info("=" * 60)
            
            return True
            
        except Exception as e:
            end_time = time.time()
            duration = end_time - start_time
            
            self.logger.error("=" * 60)
            self.logger.error(f"💥 P10 页面构建失败: {e} (耗时: {duration:.2f}秒)")
            self.logger.error("=" * 60)
            
            return False

def main():
    """主函数"""
    # 确保在正确的目录下运行
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # 创建构建器并运行
    try:
        builder = P10Builder()
        success = builder.run()
        
        if success:
            print("\n✅ P10 页面构建成功！")
            print(f"📁 输出目录: {Path(builder.config['project']['output_dir']).absolute()}")
            return 0
        else:
            print("\n❌ P10 页面构建失败！")
            print("📋 请查看日志文件获取详细信息")
            return 1
            
    except KeyboardInterrupt:
        print("\n⚠️  构建被用户中断")
        return 130
    except Exception as e:
        print(f"\n💥 构建器启动失败: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())