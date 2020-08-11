import time

from selenium import webdriver

def excute():
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    username = '13106549170'
    password = '123456'
    driver = webdriver.Chrome()
    driver.get(url=url)
    driver.implicitly_wait(5)
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pwd').send_keys(password)
    code = input('请输入验证码')
    driver.find_element_by_id('code').send_keys(code)
    driver.find_element_by_id('denglu').click()
    time.sleep(8)
    driver.quit()
    pass

if __name__ == '__main__':
    excute()
    pass