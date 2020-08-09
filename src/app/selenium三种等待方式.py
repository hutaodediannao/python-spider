from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

url = 'https://www.baidu.com/'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    # 隐式等待
    # driver.implicitly_wait(10)
    driver.get(url=url)
    # time.sleep(1)
    # 显示加载
    try:
        print('开始加载...')
        # kw = WebDriverWait(
        #     driver,
        #     10,
        #     0.5,
        #     EC.presence_of_element_located((By.ID, 'kw'))
        # )
        # kw.send_keys('oppo')

        kw = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))

        # print(type(kw))
        kw.send_keys('mate30 pro')
        btn = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, 'su')))
        btn.click()

        # print('加载成功')
        # driver.find_element(By.ID, 'kw').send_keys('美女图片')
        # driver.find_element_by_id('su').click()
    except:
        print('等待了10秒，没有加载出来')
        pass
    finally:
        time.sleep(5)
        driver.quit()
        pass
