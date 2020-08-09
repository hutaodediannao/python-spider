from selenium import webdriver
import time

from selenium.webdriver.common.by import By

url = 'https://www.taobao.com/'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)#最多等5秒，啥时候获取了就开始获取
    driver.get(url)
    print(driver.page_source)
    driver.find_element_by_xpath('//input[@id="q"]').send_keys('mac pro')
    # driver.find_element_by_class_name('btn-search tb-bg').click()
    searchBtn = driver.find_element_by_css_selector('div[class="search-button"]>button')
    searchBtn.click()
    # driver.find_element(By.ID, 'su')
    time.sleep(5)
    driver.quit()
    pass
