import ssl
import urllib
from copy import copy
from urllib import request, parse

from bs4 import BeautifulSoup
import xlrd
import xlwt

xlsfile = r""# 打开指定路径中的xls文件
xlsfilew = r""# 打开指定路径中的xls文件
book = xlrd.open_workbook(xlsfile)#得到Excel文件的book对象，实例化对象
sheet0 = book.sheet_by_index(0) # 通过sheet索引获得sheet对象
# print("1、",sheet0)
# sheet_name = book.sheet_names()[0]# 获得指定索引的sheet表名字
# print("2、",sheet_name)
# sheet1 = book.sheet_by_name(sheet_name)# 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定
nrows = sheet0.nrows    # 获取行总数
#
ssl._create_default_https_context = ssl._create_unverified_context

express = r"http://www.aliexpress.com"
wish = "https://www.wish.com"
for i in range(nrows):
    try:
        url = str(sheet0.row_values(i)[1])
        if url.startswith(express):
            a = url
            # req = urllib.request.Request(url)
            # resp = urllib.request.urlopen(req)
            # data = resp.read().decode('utf-8')
            # html = BeautifulSoup(data, 'html.parser')
            # # newBook = xlwt.Workbook(encoding='utf-8', style_compression=0)
            # # sheet = newBook.add_sheet('test', cell_overwrite_ok=True)
            # # sheet.write(i,3,html.find(attrs={'id':'j-sku-discount-price'}).string)
            # # sheet.write(i,4,html.find(attrs={'id':'j-order-num'}).string.split(" ")[0])
            # print(i,html.find(attrs={'id':'j-sku-discount-price'}).string, html.find(attrs={'id':'j-order-num'}).string.split(" ")[0])
        if url.startswith(wish):
            uri = 'hhttps://www.wish.com/api/product/get'
            data = {'cid':urllib.request.Request(uri+url.split('=')[1]),
                    "request_sizing_chart_info": "true",
                    "do_not_track":"false",
                    "_xsrf":"2|95ddfa19|eed70d6037568189219192cea00f8365|1542372349"}
            headers = {
                #heard部分直接通过chrome部分request header部分
                'Accept':'application/json, text/plain, */*',
                'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'Connection':'keep-alive',
                'Content-Length':'14', #get方式提交的数据长度，如果是post方式，转成get方式：【id=wdb&pwd=wdb】
                'Content-Type':'application/x-www-form-urlencoded',
                'Referer':'http://10.1.2.151/',
                'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
            }

            resp = urllib.request.urlopen(req)
            data = resp.read().decode('utf-8')
            html = BeautifulSoup(data, 'html.parser')
            data = parse.urlencode(data).encode('utf-8')
            req = request.Request(url, headers=headers, data=data)
            page = request.urlopen(req).read()
            page = page.decode('utf-8')

            # newBook = xlwt.Workbook(encoding='utf-8', style_compression=0)
            # sheet = newBook.add_sheet('test', cell_overwrite_ok=True)
            # sheet.write(i,3,html.find(attrs={'id':'j-sku-discount-price'}).string)
            # sheet.write(i,4,html.find(attrs={'id':'j-order-num'}).string.split(" ")[0])
            print(i,html.find(attrs={'class':'PurchaseContainer__ActualPrice-liXyad cRbBob'}).string, html.find(attrs={'class':'PurchaseContainer__RatingCount-bCsggw chcbqJ'}).string.split(" ")[0])
    except:
        print(i,' ' , ' ')
# # newBook.save(xlsfilew)

uri = 'hhttps://www.wish.com/api/product/get'
data = {'cid': urllib.request.Request(uri + url.split('=')[1]),
        "request_sizing_chart_info": "true",
        "do_not_track": "false",
        "_xsrf": "2|95ddfa19|eed70d6037568189219192cea00f8365|1542372349mmmm"}
headers = {
    # heard部分直接通过chrome部分request header部分
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '14',  # get方式提交的数据长度，如果是post方式，转成get方式：【id=wdb&pwd=wdb】
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://10.1.2.151/',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
}

