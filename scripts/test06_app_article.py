import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestAppArticle:
    def setup_class(self):
        driver = GetDriver.get_app_driver()
        self.page_in = PageIn(driver)
        self.page_in.page_get_PageAppLogin().page_app_login_success()
        self.article = self.page_in.page_get_PageAppArticle()

    def teardown_class(self):
        GetDriver.quit_app_driver()

    @pytest.mark.parametrize("click_text,title", read_yaml("app_article.yaml"))
    def test_app_article(self, click_text, title):
        try:
            self.article.page_app_article(click_text, title)
        except Exception as e:
            log.error(e)
            self.article.base_get_img()
            raise
