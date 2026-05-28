import allure
from selenium.webdriver.support.wait import WebDriverWait
from tools.get_log import GetLog
import os

log = GetLog.get_logger()


class Base:
    def __init__(self, driver):
        log.info("正在初始化driver: {}".format(driver))
        self.driver = driver

    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(*loc)
        )

    def base_input(self, loc, value):
        el = self.base_find(loc)
        log.info("正在对：{} 元素执行清空操作！".format(loc))
        el.clear()
        log.info("正在对：{} 元素执行输入:{} 操作！".format(loc, value))
        el.send_keys(value)

    def base_click(self, loc):
        log.info("正在对：{} 元素执行点击操作！".format(loc))
        self.base_find(loc).click()

    def base_get_text(self, loc):
        log.info("正在对：{} 元素获取文本操作！".format(loc))
        text = self.base_find(loc).text
        log.info("获取的文本值：{}".format(text))
        return text

    def base_get_img(self):
        img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "image", "err.png")
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        self.driver.get_screenshot_as_file(img_path)
        with open(img_path, "rb") as f:
            allure.attach("错误原因：", f.read(), allure.attachment_type.PNG)
