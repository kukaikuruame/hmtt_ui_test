import pytest
import os
import sys

# 添加项目根目录到系统路径
sys.path.insert(0, os.path.dirname(__file__))


def run_all_tests():
    """运行所有测试"""
    pytest.main([
        "-v",
        "--tb=short",
        "--html=./reports/report.html",
        "--self-contained-html",
        "--alluredir=./reports/allure"
    ])


def run_web_tests():
    """只运行Web端测试（自媒体+后台管理）"""
    pytest.main([
        "-v",
        "--tb=short",
        "./scripts/test01_mp_login.py",
        "./scripts/test02_mp_article.py",
        "./scripts/test03_mis_login.py",
        "./scripts/test04_mis_audit.py"
    ])


def run_app_tests():
    """只运行APP端测试"""
    pytest.main([
        "-v",
        "--tb=short",
        "./scripts/test05_app_login.py",
        "./scripts/test06_app_article.py"
    ])


def run_by_marker(marker):
    """根据标记运行测试"""
    pytest.main([
        "-v",
        "--tb=short",
        "-m", marker
    ])


if __name__ == '__main__':
    # 默认运行所有测试
    run_all_tests()
