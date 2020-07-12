from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class IndexPage(object):
    def __init__(self, driver):
        self.driver = driver

    def isExist_logout_ele(self):
        log_out_but = "//a[@href='/Index/logout.html']"
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, log_out_but)))
            return True
        except:
            return False

    # 选标 - 默认选择第一个
    def click_first_bid(self):
        pass

    # 随机选择一个标
    def click_bid_by_random(self):
        # 找到所有的标
        eles = self.driver.find_elements()
        index = random.randint(0, len(eles)-1)
        eles[index].click()












