from lxml import etree
import requests

url = 'https://www.neihanba.com/dz/'
urlP = 'https://www.neihanba.com/dz/list_%d.html'


def test():
    for i in range(1, 10):
        if i == 1:
            urlt = url
        else:
            urlt = urlP % (i)
        response = requests.get(urlt)
        response.encoding = 'gb2312'
        content = response.text
        html = etree.HTML(content)
        result = html.xpath('//ul[@class="piclist longList"]/li')
        print(len(result))
        for li in result:
            title = li.xpath('.//h4/a/b/text()')[0]
            say = li.xpath('.//div[@class="f18 mb20"]/text()')[0]
            time = li.xpath('./div[@class="ft"]/span/text()')[0]
            print(title)
            print(say)
            print(time)
            print("=================================分割线=====================================")







if __name__ == '__main__':
    test()
