import pytest
from tools.get_driver import GetDriver


@pytest.fixture(scope="session", autouse=True)
def setup_env():
    """测试环境初始化"""
    yield
    # 测试结束后关闭所有驱动
    GetDriver.quit_web_driver()
    GetDriver.quit_app_driver()
