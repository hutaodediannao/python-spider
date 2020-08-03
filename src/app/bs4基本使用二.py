import re

import bs4
from bs4 import BeautifulSoup

html_doc =  """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story bg range">Once upon a time there were three little sisters; and their names were</p>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
<p>and they lived at the bottom of a well.</p>
<p class="story custom_bg">...</p>
"""

soup = BeautifulSoup(html_doc.encode(encoding='utf-8'), features="html.parser", from_encoding="utf-8")
# links = soup.find_all('a')
# print('所有的链接')
# for link in links:
#     print(link.name, link['href'], link.get_text())

# 根据文本内容匹配
# elsie_link = soup.find('a', text='Lacie')
# print(elsie_link['href'])

# 根据正则表达式匹配
# tiLink = soup.find_all('a', href=re.compile(r'cie'))
# print(tiLink)

# targetLinks = soup.find_all('p')
# # print(len(targetLink))
# for p in targetLinks:
#     print(p.text)

pclass = soup.find('p', class_='story', )
# print(pclass.get_text())
print(pclass['class'])