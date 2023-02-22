from selenium import webdriver
from selenium.webdriver.common.by import By

from Until.ReadIni import LoadingConfig


def test_AdminLogin():
    read=LoadingConfig()
    con=read.readini()
    driver = webdriver.Chrome()
    # url=str(con['env']['uat_url'])
    url='https://oasis-uat.mercedes-benz.com.cn'

    print(url)

    driver.get(url)
    driver.implicitly_wait(100)
    driver.find_element(by=By.ID,value='userid').send_keys(con['Role']['ADMIN'])
    driver.find_element(by=By.ID,value='next-btn').click()

