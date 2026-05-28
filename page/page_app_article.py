from base.app_base import AppBase
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppArticle(AppBase):
    def page_click_channel(self, click_text):
        self.app_base_right_wipe_left(page.app_channel_area, click_text)

    def page_click_article(self, title):
        self.app_base_down_wipe_up(page.app_article_area, click_text=title)

    def page_app_article(self, find_text, title):
        log.info("正在调用查询文章业务方法 文章频道：{} 文章title:{}".format(find_text, title))
        self.page_click_channel(find_text)
        self.page_click_article(title)
