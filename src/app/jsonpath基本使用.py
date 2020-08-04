import json

import jsonpath

jsStr = '''{ "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    },
    "author": "sb"
  }
}'''

def test():
    jsobj= json.loads(jsStr)
    # title = jsonpath.jsonpath(jsobj, '$.store.book[1]')
    # title = jsonpath.jsonpath(jsobj, '$.store.book[1].title')
    # 获取所有书的作者[*]匹配当前节点下所有
    # title = jsonpath.jsonpath(jsobj, '$.store.book[*].author')
    # title = jsonpath.jsonpath(jsobj, '$..author')
    # title = jsonpath.jsonpath(jsobj, '$.store.*')
    # title = jsonpath.jsonpath(jsobj, '$.store..price')
    # title = jsonpath.jsonpath(jsobj, '$..book[2]')
    # 获取最后一本书
    # title = jsonpath.jsonpath(jsobj, '$..book[(@.length-1)]')
    # title = jsonpath.jsonpath(jsobj, '$..book[-1:]')
    # 获取1到3的书的作者
    # title = jsonpath.jsonpath(jsobj, '$..book[1:3].author')
    # 过滤掉isbn是空的
    # title = jsonpath.jsonpath(jsobj, '$..book[?(@.isbn)]')
    # 获取价格小于9的书的数据
    # title = jsonpath.jsonpath(jsobj, '$..book[?(@.price<9)]')
    title = jsonpath.jsonpath(jsobj, '$..*')





    print(title)






    pass

if __name__ == '__main__':
    test()
    pass
