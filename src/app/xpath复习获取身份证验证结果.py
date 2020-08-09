import requests
from threading import Thread

from lxml import etree


def excute(url: str):
    response = requests.get(url=url,)
    response.encoding = 'utf-8'
    content = response.text
    html = etree.HTML(content)
    result = html.xpath('//div//tr/td/font/text()')
    print(result[0])
    pass


if __name__ == '__main__':
    url = 'https://shenfenzheng.51240.com/'
    t = Thread(target=excute, args=(url,))
    t.start()
    pass
