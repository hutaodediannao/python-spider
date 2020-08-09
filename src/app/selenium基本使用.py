from selenium import webdriver
import time

url = 'http://www.qq.com'
if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='E:\python\chromedriver.exe')
    driver.get(url)
    time.sleep(2)
    # driver.maximize_window()
    # driver.set_window_size(300, 300)
    driver.set_window_rect(100, 100, 300, 300)
    time.sleep(3)
    driver.save_screenshot('./qq.png')
    driver.close()
    pass
