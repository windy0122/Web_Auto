from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class BidPage(object):
    def __init__(self, driver):
        self.driver = driver

    # 投资
    def invest(self):
        pass

    # 获取用户余额
    def get_user_money(self):
        pass

    # 投资成功提示框，点击查看并激活
    def click_activeButton_on_success_popup(self):
        pass

    # 错误的提示框 - 页面中间
    def get_errorMsg_from_pageCenter(self):
        pass

    # 获取提示信息，投标按钮上方的
    def get_errorMsg_from_investButton(self):
        pass








