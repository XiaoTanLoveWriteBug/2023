from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By




def test_AdminLogin():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach',True)#设置为浏览器不关闭
    driver = webdriver.Chrome(chrome_options=option)
    url='https://oasis-uat.mercedes-benz.com.cn'
    driver.get(url)
    driver.implicitly_wait(100)
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div/div[1]/div/div/div[1]/form/div[2]/div[1]/div/input').send_keys('OAADMIN')
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div/div[1]/div/div/div[1]/form/div[2]/div[1]/button').click()
    driver.find_element(by=By.ID,value='password').clear()
    driver.find_element(by=By.ID,value='password').send_keys('Daimle2023Q1!')
    driver.find_element(by=By.ID,value='loginSubmitButton').click()

    # 输出当前窗口句柄
    baidu_handle = driver.current_window_handle
    # 获取当前窗口句柄集合（列表类型）
    handles = driver.window_handles
    print(handles)  # 输出句柄集合

def test_RegionLogin():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach',True)#设置为浏览器不关闭
    driver = webdriver.Chrome(chrome_options=option)
    url='https://oasis-uat.mercedes-benz.com.cn'
    driver.get(url)
    driver.implicitly_wait(100)
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div/div[1]/div/div/div[1]/form/div[2]/div[1]/div/input').send_keys('OASISQI')
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/main/div/div[1]/div/div/div[1]/form/div[2]/div[1]/button').click()
    driver.find_element(by=By.ID,value='password').clear()
    driver.find_element(by=By.ID,value='password').send_keys('Daimle2023Q1!')
    driver.find_element(by=By.ID,value='loginSubmitButton').click()
    print(driver.window_handles)
    # 新开一个窗口，通过执行js来新开一个窗口
    js = 'window.open("https://www.baidu.com");'
    driver.execute_script(js)
    # 输出当前窗口句柄
    baidu_handle = driver.current_window_handle
    # 获取当前窗口句柄集合（列表类型）
    handles = driver.window_handles
    print(handles)  # 输出句柄集合
