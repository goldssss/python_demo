from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('hello world')

def hello(request):
    return render(request,"demo01.html")

def google(request):
    return render(request,"google.html")