import time

from selenium import webdriver

url = 'https://www.douban.com/'
def excute():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    frame = driver.find_element_by_xpath('//div[@class="login"]/iframe')
    driver.switch_to.frame(frame)
    # print(frame)
    account = driver.find_element_by_class_name('account-tab-account')
    print(account)
    account.click()
    time.sleep(2)
    driver.find_element_by_id('username').send_keys('13106549170')
    driver.find_element_by_id('password').send_keys('13579taohu')
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="account-form-field-submit "]/a[@class="btn btn-account btn-active"]')\
        .click()
    time.sleep(8)
    driver.quit()

if __name__ == '__main__':
    excute()
    pass