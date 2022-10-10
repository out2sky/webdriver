
from lib2to3.pgen2 import driver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


def main():
    driver = webdriver.Chrome()
    time.sleep(1)

    driver.get("https://www.baidu.com")
    driver.find_element('id','kw').send_keys('try')
    driver.find_element('id',"kw").send_keys(Keys.ENTER)
    time.sleep(5)

    driver.quit()












main()