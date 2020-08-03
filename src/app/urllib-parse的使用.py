from urllib import parse

if __name__ == '__main__':
    parmas = {
        'name': '胡涛',
        'age': 30,
        'sex': '男'
    }
    # parmas = parse.urlencode(parmas)
    # print(type(parmas))


    parmas2 = parse.urlencode(parmas).encode()
    print(type(parmas2))

