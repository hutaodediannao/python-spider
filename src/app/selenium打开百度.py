from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.baidu.com/'

if __name__ == '__main__':
    x, y = 100, 100
    while True:
        driver = webdriver.Chrome()
        driver.set_window_rect(x, y, width=400, height=400)
        driver.implicitly_wait(10)
        driver.get(url)
        driver.find_element(By.ID, 'kw').send_keys('小米手机')
        driver.find_element(By.ID, 'su').click()
        time.sleep(1)
        x += 100
        y += 100
