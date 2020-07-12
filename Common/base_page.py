# 封装基本函数 -- 执行日志、异常处理、失败截图
# 所有页面公共的部分
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from Common.project_path import *
import time


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, wait_time=30, poll_frequency=0.5, doc=''):

        '''
        :param locator: 元素定位，元组形式（元素定位类型、元素定位方式）
        :param times:
        :param poll_frequency:
        :param doc:模块名_页面操作_操作名称
        :return:
        '''

        logging.info('等待元素{0}可见'.format(locator))
        try:
            # 开始等待时间
            start_time_now = datetime.datetime.now()
            WebDriverWait(self.driver, wait_time, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待时间
            end_time_now = datetime.datetime.now()
            wait_time = (end_time_now - start_time_now).seconds
            logging.info('等待结束，等待时间为：{0}'.format(wait_time))
        except:
            logging.exception('等待元素可见失败')
            # 截图
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=''):
        logging.info('查找元素：{}'.format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception('查找元素失败！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        logging.info('{0}点击元素：{1}'.format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception('点击元素失败！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=''):
        ele = self.get_element(locator, doc)
        try:
            ele.send_keys(text)
        except:
            logging.exception('输入失败！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素文本操作
    def get_text(self, locator, doc=''):
        ele = self.get_element(locator, doc)
        try:
            return ele.text
        except:
            logging.exception('获取文本失败！')
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, doc=''):
        ele = self.get_element(locator, doc)
        try:
            return ele.get_accttibute(attr)
        except:
            logging.exception('获取元素属性失败！')
            # 截图
            self.save_screenshot(doc)
            raise

    # alert处理
    def alert_action(self):
        pass

    # iframe处理
    def switch_iframe(self):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    # 窗口切换

    # 截图
    def save_screenshot(self, doc):
        # 截图当前时间
        time_image = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())
        file_name_image = image_screen_path + '{0}_{1}.png'.format(doc, time_image)
        try:
            self.driver.save_screenshot(file_name_image)
            logging.info('截取网页成功，文件路径为：{}'.format(file_name_image))
        except:
            logging.info('截图失败')








