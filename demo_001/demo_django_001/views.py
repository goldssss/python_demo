import urllib

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    request.path='google.hk'
    url = "https://www.google.com.hk/webhp?ie=UTF-8&rct=j"
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    data = resp.read().decode('utf-8')
    return HttpResponse(data)

def hello(request):
    return render(request,"demo01.html")

def google(request):
    return render(request,"google.html")