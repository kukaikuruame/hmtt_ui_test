from base.web_base import WebBase
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisLogin(WebBase):
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    def page_input_pwd(self, pwd):
        self.base_input(page.mis_pwd, pwd)

    def page_click_login_btn(self):
        js = "document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)
        self.base_click(page.mis_login_btn)

    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    def page_mis_login(self, username, pwd):
        log.info("正在调用后台管理系统登录业务方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        log.info("正在调用后台管理系统成功登录依赖方法，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
