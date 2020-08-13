import time

from selenium import webdriver
from PIL import Image

def excute():
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url=url)
    img = driver.find_element_by_id('imgCode')
    # 截屏
    driver.save_screenshot('./code.png')
    image = Image.open('./code.png')
    loc = img.location
    size = img.size
    print(loc, size)
    rec=(loc['x'], loc['y'], loc['x']+size['width'], loc['y']+size['height'])
    rec=(820, 260, 820+size['width']+10, 260+size['height'])
    captcha = image.crop(rec)
    # 保存到文件中
    captcha.save('./captcha.png')
    captcha.show()
    time.sleep(5)
    driver.quit()



if __name__ == '__main__':
    excute()
    pass
