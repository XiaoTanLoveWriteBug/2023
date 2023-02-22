from _pytest import assertion
from selenium.webdriver.chrome import webdriver


def test_assert():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach',True)#设置为浏览器不关闭
    driver = webdriver.Chrome(chrome_options=option)
    url='https://www.baidu.com'
    driver.get(url)
    driver.implicitly_wait(100)
