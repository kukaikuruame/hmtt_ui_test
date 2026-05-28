from time import sleep
from base.web_base import WebBase
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisAudit(WebBase):
    article_id = None

    def page_click_info_manage(self):
        sleep(1)
        self.base_click(page.mis_info_manage)

    def page_click_content_audit(self):
        sleep(1)
        self.base_click(page.mis_content_audit)

    def page_input_title(self, title):
        self.base_input(page.mis_title, title)

    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    def page_click_status(self, placeholder_text="请选择状态", click_text="待审核"):
        self.web_base_click_element(placeholder_text, click_text)

    def page_click_find(self):
        self.base_click(page.mis_find)
        sleep(2)

    def page_get_article_id(self):
        return self.base_get_text(page.mis_article_id)

    def page_click_pass_btn(self):
        self.base_click(page.mis_pass)

    def page_click_confirm_pass(self):
        sleep(1)
        self.base_click(page.mis_confirm_pass)

    def page_mis_audit(self, title, channel):
        log.info("正在调用审核文章业务方法，title: {} channel：{}".format(title, channel))
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_find()
        self.article_id = self.page_get_article_id()
        print("获取的文章id为：", self.article_id)
        self.page_click_pass_btn()
        self.page_click_confirm_pass()

    def page_assert_audit(self):
        log.info("正在调用断言业务操作方法")
        sleep(3)
        self.page_click_status(click_text="审核通过")
        self.page_click_find()
        return self.web_base_is_exist(self.article_id)
