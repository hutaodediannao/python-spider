"""中国天气网爬取并视图显示最低气温城市"""
import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3554.0 Safari/537.36"}
ALL_DATA = []


def detail_urls(url):
    rep = requests.get(url=url, headers=HEADERS)
    text = rep.content.decode(encoding="utf-8")
    # 港澳表格标签残缺需要补缺能力强的html5lib补齐表格标签
    soup = BeautifulSoup(text, "html5lib")
    # 找到第一个属性为conMidtab的div标签
    commidtab = soup.find("div", class_="conMidtab")
    # 找到这个div下的所有table
    tables = commidtab.find_all("table")
    # 循环每一个table
    for table in tables:
        # 排除介绍部分
        trs = table.find_all("tr")[2:]
        # 省份和直辖市两种情况
        for index, tr in enumerate(trs):
            tds = tr.find_all("td")
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            # 获取所有文本并去掉空格
            city = list(city_td.stripped_strings)[0]
            min_temp_td = tds[-2]
            min_temp = list(min_temp_td.stripped_strings)[0]
            max_temp_td = tds[-5]
            max_temp = list(max_temp_td.stripped_strings)[0]
            ALL_DATA.append({"city": city, "min_temp": int(min_temp), "max_temp": int(max_temp)})


def spider():
    base_url = "http://www.weather.com.cn/textFC/{}.shtml"
    # 页数较少所以直接拿
    address = ["hb", "db", "hd", "hz", "hn", "xb", "xn", "gat"]
    for i in range(len(address)):
        url = base_url.format(address[i])
        # 将生成的传递给页面解析函数
        get_detail_urls = detail_urls(url)
    ALL_DATA.sort(key=lambda data: data["min_temp"])
    datas = ALL_DATA[0:10]
    cities = list(map(lambda x: x["city"], datas))
    min_temp = list(map(lambda x: x["min_temp"], datas))
    max_temp = list(map(lambda x: x["max_temp"], datas))
    bar = Bar("中国最低气温排行榜")
    bar.add("最低气温", cities, min_temp, mark_line=["average"], mark_point=["max", "min"])
    bar.add("最高气温", cities, max_temp, mark_line=["average"], mark_point=["max", "min"])
    bar.render("temperature.html")


if __name__ == '__main__':
    spider()