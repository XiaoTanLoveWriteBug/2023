# 截图封装
import os

from selenium.webdriver.chrome import webdriver


class screensho():
    def __init__(self):
        self.screenshot_path='photo';
        self.driver=webdriver.WebDriver()


    def TestRun(self):
        # 增加断言，断言成功则通过，断言失败则截图
#         if word in driver.page_source:
#         print('testcase is pass!')
#      else:
        self.driver.get_screenshot_as_file(self.screenshot_path+".png")