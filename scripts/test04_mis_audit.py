import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestMisAudit:
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_mis)
        self.page_in = PageIn(driver)
        self.page_in.page_get_PageMisLogin().page_mis_login_success()
        self.audit = self.page_in.page_get_PageMisAudit()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def test_mis_audit(self, title=page.title, channel=page.channle):
        self.audit.page_mis_audit(title, channel)
        try:
            assert self.audit.page_assert_audit()
        except Exception as e:
            log.error(e)
            self.audit.base_get_img()
            raise
