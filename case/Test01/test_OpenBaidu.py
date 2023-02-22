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
    print(title)
    js='window.open("https://www.baidu.com");'
    driver.execute_script(js)
    driver.window_handles
# driver.back()
    driver.find_element(by=By.ID, value="su").click()
    driver.find_element(by=By.ID,value='su').click()
    # driver.quit()











