import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMisLogin:
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_mis)
        self.mis = PageIn(driver).page_get_PageMisLogin()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,pwd,expect", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, pwd, expect):
        self.mis.page_mis_login(username, pwd)
        try:
            assert expect in self.mis.page_get_nickname()
        except Exception as e:
            log.error(e)
            self.mis.base_get_img()
            raise
