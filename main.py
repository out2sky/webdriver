

import os

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def make_webdriver():
    option = Options()
    # option.add_argument('--headless')
    # option.add_argument('--no-sandbox')
    # option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--remote-debugging-port=9222")
    
    if os.name == 'posix':
        web_driver_file = r"./chromedriver"
    else:
        web_driver_file = r"chromedriver.exe"

    return webdriver.Chrome(web_driver_file,chrome_options=option)


def main():


    driver = make_webdriver()
    time.sleep(1)

    driver.get("https://www.baidu.com")
    driver.find_element('id','kw').send_keys('try')
    # driver.find_element('id',"kw").send_keys(Keys.ENTER)
    driver.find_element('id','su').click()
    time.sleep(5)

    driver.quit()




main()
