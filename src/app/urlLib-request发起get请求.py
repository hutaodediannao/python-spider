import urllib
from urllib import request, parse

if __name__ == '__main__':
    url = 'https://cart.taobao.com/cart.htm?%s'
    headers = {
        'Authority': 'cart.taobao.com',
        'method': 'GET',
        'path': '/cart.htm?spm=a21bo.2017.1997525049.1.5af911d93f9ruR&from=mini&pm_id=1501036000a02c5c3739',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh,zh-CN;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'miid=157337882132893791; cna=MGGPF8KmQD0CAbcRPyFSlJyU; t=264e6d76521b19aa113bae3a29427abd; _samesite_flag_=true; cookie2=166651def51881f1892ac76105aa4a06; _tb_token_=ea11168b574e4; sgcookie=EVzw5I0Ii2Lodh7JZXogX; unb=2651533269; uc3=nk2=2VqW1EsKRXfSqw%3D%3D&id2=UU6kUgjaE7HFqw%3D%3D&vt3=F8dBxGypM7mkdm%2FGINI%3D&lg2=URm48syIIVrSKA%3D%3D; csg=d709f484; lgc=%5Cu80E1%5Cu6D9B%5Cu7684%5Cu8D26%5Cu6237; cookie17=UU6kUgjaE7HFqw%3D%3D; dnk=%5Cu80E1%5Cu6D9B%5Cu7684%5Cu8D26%5Cu6237; skt=8d6c297b99a95b01; existShop=MTU5NjI5ODQ3OQ%3D%3D; uc4=id4=0%40U2xpUOjtSXE7McotEXwOY50xq%2BeF&nk4=0%4027w5VHpOylJmToOvV1DHjpD19Mo4; tracknick=%5Cu80E1%5Cu6D9B%5Cu7684%5Cu8D26%5Cu6237; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=%E6%88%B799; _nk_=%5Cu80E1%5Cu6D9B%5Cu7684%5Cu8D26%5Cu6237; cookie1=WqOli%2BLhRZuXZPY244DZEhPJTmz2Yhb%2F7Z%2FwsZ4d1D8%3D; ubn=p; mt=ci=1_1; thw=cn; ucn=center; _m_h5_tk=609fca14373101a53a9edaff1972dce1_1596306771853; _m_h5_tk_enc=460d2ae71b24693ffd0b647201ba09d5; v=0; uc1=cookie14=UoTV6hixISuRQg%3D%3D&cookie21=VT5L2FSpccLuJBreK%2BBd&existShop=false&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cart_m=0&pas=0; isg=BMPDNkrSmA8cnVR8GaI5mquaUodtOFd65_a-R_WgHyKZtOPWfQjnyqEmLkz6D69y; l=eBr-eGelOxY91HcBBOfanurza77OSIRYYuPzaNbMiOCPOBfB5pofWZo5WHL6C3GNh6JwR3lil4lwBeYBqQAonxvOUKaOYMkmn; tfstk=c9XhBjqxv6RBbROGGJ9C4ydAGH2Aw-FeRTWNQ9ESplKEBA102fl4ODEMJwX-N',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    }
    data = {
        'spm': 'a21bo.2017.1997525049.1.5af911d93f9ruR',
        'from': 'mini',
        'pm_id': '1501036000a02c5c3739'
    }

    parmas = parse.urlencode(data)

    # Request请求头
    request = request.Request(url=url%(parmas), headers=headers)
    # 请求头
    response = urllib.request.urlopen(request)
    result = str(response.read()).encode(encoding='utf-8')
    print(result)
