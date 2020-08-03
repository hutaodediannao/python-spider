import requests

if __name__ == '__main__':
    url = 'https://hao.360.com/?a1004'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh,zh-CN;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '__guid=234898968.156758987606731000.1596334456629.4397; sessionID=234898968.3523584721251691500.1596334457443.0486; customEng=8-2; _uc_m2=31fcbe0b78a21d19f12a37d1837f0fded785479d2bcd; _uc_mid=64f1a479fb797f27fa2a2cd8dfc6ee29; __huid=11Dnl1vdETKbWlQTrmlt79WhBr6qZCsP8%2BbsaXCMf96rY%3D; __hsid_t=cf727279ff0e187a_t; __hsid=cf727279ff0e187a; count=4; test_cookie_enable=null',
        'Host': 'hao.360.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers, verify=False).text
    print(response)
