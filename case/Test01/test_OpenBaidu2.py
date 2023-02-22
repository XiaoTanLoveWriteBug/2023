# from selenium import webdriver
#
# from time import sleep
#
# from selenium.webdriver import Keys
#
# # class test_serach()
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# elem1 = driver.find_element_by_name("wd")
# elem1.send_keys(" and some", Keys.ARROW_DOWN)
# elem2= driver.find_element_by_id("su").click()
#
# assert "No results found." not in driver.page_source
# sleep(20)
# driver.quit()
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_open():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    driver.implicitly_wait(10)
    driver.find_element(by=By.ID, value="kw").send_keys("7K7K")
    driver.maximize_window()
    title=driver.title
    driver.window_handles
    print(title)
# driver.back()
    driver.find_element(by=By.ID, value="su").click()
    driver.find_element(by=By.ID,value='su').click()
    driver.quit()











