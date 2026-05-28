from time import sleep
from base.web_base import WebBase
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpArticle(WebBase):
    def page_click_content_manage(self):
        sleep(2)
        self.base_click(page.mp_content_manage)

    def page_click_publish_article(self):
        sleep(1)
        self.base_click(page.mp_publish_article)

    def page_input_title(self, title):
        sleep(1)
        self.base_input(page.mp_title, title)

    def page_input_content(self, content):
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        sleep(1)
        self.base_input(page.mp_content, content)
        self.driver.switch_to.default_content()

    def page_click_cover(self):
        sleep(1)
        self.base_click(page.mp_cover)

    def page_click_channel(self):
        self.web_base_click_element(placeholder_text="请选择", click_text=page.channle)

    def page_click_submit(self):
        self.base_click(page.mp_submit)

    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    def page_mp_article(self, title, content):
        log.info("正在调用发布文章业务方法，文章标题：{} 文章内容：{}".format(title, content))
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()
