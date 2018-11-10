import ssl
import urllib
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        url = "https://www.google.com"+request.get_full_path()
        ssl._create_default_https_context = ssl._create_unverified_context
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url,headers=headers)
        resp = urllib.request.urlopen(req)
        data = resp.read()
    except:
        print('request error. path>>>' + request.get_full_path())
    return HttpResponse(data)

def hello(request):
    print(request.get_full_path())
    return render(request,"demo01.html")

def google(request):
    return render(request,"google.html")

