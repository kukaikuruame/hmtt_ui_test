from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class AppBase(Base):
    def app_base_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=3)
            log.info("在app页面中找到指定元素！")
            print("找到：{}元素啦!".format(loc))
            return True
        except:
            log.error("没有在app页面中找到指定元素！")
            print("未找到：{}元素！".format(loc))
            return False

    def app_base_right_wipe_left(self, loc_area, click_text):
        log.info("正在调用从右向左滑动屏幕方法")
        el = self.base_find(loc_area)
        y = el.location.get("y")
        width = el.size.get("width")
        height = el.size.get("height")
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5
        loc = By.XPATH, "//android.widget.HorizontalScrollView/*[contains(@text,'{}')]".format(click_text)

        while True:
            page_source = self.driver.page_source
            try:
                sleep(2)
                el = self.base_find(loc, timeout=3)
                print("找到：{} 元素啦！".format(click_text))
                sleep(2)
                el.click()
                break
            except:
                print("未找到：{}元素！".format(click_text))
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if page_source == self.driver.page_source:
                print("滑到最后一屏幕，未到找元素！")
                raise NoSuchElementException

    def app_base_down_wipe_up(self, loc_area, click_text):
        log.info("正在调用从下向上滑动屏幕方法")
        el = self.base_find(loc_area)
        width = el.size.get("width")
        height = el.size.get("height")
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2
        loc = By.XPATH, "//*[@bounds='[0,520][1440,2288]']//*[contains(@text,'{}')]".format(click_text)

        while True:
            page_source = self.driver.page_source
            try:
                el = self.base_find(loc, timeout=3)
                print("找到：{} 元素啦！，文章标题为：{}".format(click_text, el.text))
                el.click()
                break
            except:
                print("未找到：{}元素！".format(click_text))
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if page_source == self.driver.page_source:
                print("滑到最后一屏幕，未到找元素！")
                raise NoSuchElementException
