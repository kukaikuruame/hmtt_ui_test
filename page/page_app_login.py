from time import sleep
from base.app_base import AppBase
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageAppLogin(AppBase):
    def page_input_phone(self, phone):
        self.base_input(page.app_phone, phone)

    def page_input_code(self, code):
        self.base_input(page.app_code, code)

    def page_click_login_btn(self):
        sleep(2)
        self.base_click(page.app_login_btn)

    def page_is_login_success(self):
        return self.app_base_is_exist(page.app_me)

    def page_app_login(self, phone, code):
        log.info("正在调用app应用登录业务方法 手机号:{} 验证码: {}".format(phone, code))
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()

    def page_app_login_success(self, phone="13812345678", code="246810"):
        log.info("正在调用app应用登录业务方法 手机号:{} 验证码: {}".format(phone, code))
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()
