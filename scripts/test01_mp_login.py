import pytest
from time import sleep
from tools.get_log import GetLog
from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpLogin:
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_mp)
        self.mp = PageIn(driver).page_get_PageMpLogin()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,code,expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, code, expect):
        self.mp.page_mp_login(username, code)
        sleep(3)  # 等待登录完成
        # 调试：截图查看登录后页面
        self.mp.base_get_img()
        try:
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            print("错误原因：", e)
            self.mp.base_get_img()
            raise
