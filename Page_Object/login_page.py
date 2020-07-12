# 此页面只管理元素的操作

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.login_page_locators import LoginPageLocators as loc
from Common.base_page import BasePage


class LoginPage(BasePage):

    # 登录
    def login(self, username, passwd, rember_user=True):

        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LP.name_text))
        # self.driver.find_element(*loc.name_text).send_keys(username)
        # self.driver.find_element(*loc.pwd_text).send_keys(passwd)
        doc = '登录页面_登录功能'
        self.wait_eleVisible(loc.name_text, doc=doc)
        self.input_text(loc.name_text, username, doc)
        self.input_text(loc.pwd_text, passwd, doc)
        # 判断rember_user的值，来决定是否勾选
        if rember_user is False:
            # self.driver.find_element_by_xpath("//input[@name='remember_me']").click()
            self.click_element(loc.rember_phone_number, doc)
        # self.driver.find_element(*loc.login_button).click()
        self.click_element(loc.login_button, doc)

    # 注册
    def register_enter(self):
        pass

    # 获取登录区域的错误提示
    def get_errorMsg_from_loginArea(self):
        doc = '登录页面_获取登录错误提示'
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(*loc.error_msg))
        # return self.driver.find_element(*loc.error_msg).text
        self.wait_eleVisible(loc.error_msg, doc=doc)
        return self.get_text(loc.error_msg, doc)







