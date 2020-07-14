import unittest
from selenium import webdriver
from Page_Object.login_page import LoginPage
from Page_Object.index_page import IndexPage
from TestDatas import common_datas as cd
from TestDatas import login_datas as ld
from ddt import ddt, data
import pytest


# @ddt
@pytest.mark.usefixtures('refresh_page')
@pytest.mark.usefixtures("access_web")
class TestLogin(object):
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(cd.web_login_url)
    #     cls.driver.maximize_window()
    #     cls.lg = LoginPage(cls.driver)

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(cd.web_login_url)
    #     self.driver.maximize_window()
    #     self.lg = LoginPage(self.driver)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #
    # def tearDown(self):
    #     self.driver.refresh()

    # 正常用例 - 手机号正确登录
    @pytest.mark.smoke
    def test_login_1_success(self, access_web):
        access_web[1].login(ld.success_data['user'], ld.success_data['passwd'])
        assert IndexPage(access_web[0]).isExist_logout_ele()

    # @data(*ld.phone_data)
    # # 异常用例 - 手机号格式不正确
    # def test_login_0_wrongFormat(self, data):
    #     self.lg.login(data['user'], data['passwd'])
    #     self.assertEqual(self.lg.get_errorMsg_from_loginArea(), data['check'])
    #
    # # 异常用例，错误密码弹框
    # def test_login_wrongPwd_noReg(self):
    #     # //*[@class="layui-layer-content"]
    #     pass


