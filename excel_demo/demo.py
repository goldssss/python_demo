import ssl
import urllib
from copy import copy
from urllib import request, parse

from bs4 import BeautifulSoup
import xlrd
import xlwt

ssl._create_default_https_context = ssl._create_unverified_context

uri = 'https://www.wish.com/api/product/get'
data = {'cid':'550d3d3647a9870f41012d6b',
        'request_sizing_chart_info': 'true',
        'do_not_track': 'false',
        '_xsrf': '2|95ddfa19|eed70d6037568189219192cea00f8365|1542372349mmmm'}
headers = {
    # heard部分直接通过chrome部分request header部分
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '14',  # get方式提交的数据长度，如果是post方式，转成get方式：【id=wdb&pwd=wdb】
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://10.1.2.151/',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
    }

data = parse.urlencode(data).encode('utf-8')
req = request.Request(uri, data=data)  #POST方法
#req = request.Request('https://www.wish.com/api/product/get?cid=5b5141a7c004ad63e1597d84&request_sizing_chart_info=true&do_not_track=false')  # GET方法
page = request.urlopen(req).read()
page = page.decode('utf-8')
