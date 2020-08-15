import time

from PIL import Image
from selenium import webdriver
import pytesseract
from selenium.common.exceptions import NoSuchElementException


def getDriver():
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url=url)
    return driver


def getCaptchaCode(driver):
    img = driver.find_element_by_id('imgCode')
    # 截屏
    driver.save_screenshot('./code.png')
    image = Image.open('./code.png')
    # loc = img.location
    size = img.size
    # print(loc, size)
    # rec=(loc['x'], loc['y'], loc['x']+size['width'], loc['y']+size['height'])
    rec = (820, 260, 820 + size['width'] + 10, 260 + size['height'])
    captcha = image.crop(rec)
    # 保存到文件中
    captcha.save('./captcha.png')
    return captcha


if __name__ == '__main__':
    excute()
    pass
