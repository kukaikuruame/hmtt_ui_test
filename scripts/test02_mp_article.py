from page.page_in import PageIn
from tools.get_driver import GetDriver
import page


class TestMpArticle:
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_mp)
        self.page_in = PageIn(driver)
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        self.article = self.page_in.page_get_PageMpArticle()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def test_mp_article(self, title="test001-bj001", content="今晚炖火锅！"):
        self.article.page_mp_article(title, content)
        print("发布文章结果为：", self.article.page_get_info())
