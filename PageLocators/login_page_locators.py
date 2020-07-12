# 此页面只管理元素的定位
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    # 用户名输入框
    name_text = (By.XPATH, "//input[@name='phone']")
    # 密码输入框
    pwd_text = (By.XPATH, "//input[@name='password']")
    # 登录按钮
    login_button = (By.XPATH, "//button[@type='button']")
    # 输入框下的提示信息
    error_msg = (By.XPATH, "//div[@class='form-error-info']")
    # 弹框提示信息
    error_msg_login = (By.XPATH, "//*[@class='layui-layer-content']")
    # 登录选择记住手机号
    rember_phone_number = (By.XPATH, "//input[@name='remember_me']")



