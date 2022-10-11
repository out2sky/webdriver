
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def main():
    option = Options()
    # option.add_argument('--headless')
    # option.add_argument('--no-sandbox')
    # option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(r"./chromedriver",chrome_options=option)
    time.sleep(1)

    driver.get("https://www.baidu.com")
    driver.find_element('id','kw').send_keys('try')
    driver.find_element('id',"kw").send_keys(Keys.ENTER)
    time.sleep(5)

    driver.quit()












main()