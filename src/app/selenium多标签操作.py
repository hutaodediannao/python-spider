import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=oppo&fenlei=256&rsv_pq=f575df320001b115&rsv_t=1a7bDuzmGAs3z7nybgHjulYG9ZoJ2MYxTO7HnvhIXcY%2Ft%2BLP5jLqejW7RtA&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=5&rsv_sug1=2&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=997&rsv_sug4=2107'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)

    ta = driver.find_elements_by_xpath('//a[@data-is-main-url="true"]')[3]
    ta.click()
    time.sleep(3)
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    # driver.back()
    time.sleep(2)
    driver.quit()
    pass