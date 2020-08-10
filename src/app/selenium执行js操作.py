import time

from selenium import webdriver

url = 'https://www.douban.com'
def test():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    js = 'window.scrollTo(0, document.body.scrollHeight)'
    driver.execute_script(js)
    time.sleep(5)
    driver.quit()




    pass

if __name__ == '__main__':
    test()
    pass