from time import sleep
from selenium.webdriver.common.by import By
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class WebBase(Base):
    def web_base_click_element(self, placeholder_text, click_text):
        log.info("正在调用web专属点击封装方法")
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_text)
        self.base_click(loc)
        sleep(1)
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

    def web_base_is_exist(self, text):
        log.info("正在调用查找页面是否存在指定元素：{} 方法".format(text))
        loc = By.XPATH, "//*[text()='{}']".format(text)
        try:
            self.base_find(loc, timeout=3)
            print("找到：{} 元素啦！".format(text))
            return True
        except:
            print("没有找到：{} 元素！".format(text))
            return False
