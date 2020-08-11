import time

from selenium import webdriver

url = 'http://account.chinaunix.net/login'

def excute():
    username = '18513106743'
    password = '31415926abc'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element_by_id('username').send_keys(username)
    time.sleep(2)
    driver.find_element_by_id('password').send_keys(password)
    time.sleep(3)
    driver.find_element_by_id('btnSubmit').click()
    time.sleep(10)
    driver.quit()

    pass

if __name__ == '__main__':
    excute()
    pass