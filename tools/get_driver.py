from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from appium.options.android import UiAutomator2Options
from appium import webdriver as appium_webdriver
import config


class GetDriver:
    __web_driver = None
    __app_driver = None

    @classmethod
    def get_web_driver(cls, url):
        if cls.__web_driver is None:
            options = Options()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            cls.__web_driver = webdriver.Chrome(options=options)
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            options = UiAutomator2Options()
            options.platform_name = 'Android'
            options.platform_version = '5.1'
            options.device_name = '192.168.56.101:5555'
            options.app_package = config.appPackage
            options.app_activity = config.appActivity
            options.no_reset = True
            cls.__app_driver = appium_webdriver.Remote(config.appium_server, options=options)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
            cls.__app_driver = None


if __name__ == '__main__':
    from time import sleep
    GetDriver.get_app_driver()
    sleep(1)
    GetDriver.quit_app_driver()
