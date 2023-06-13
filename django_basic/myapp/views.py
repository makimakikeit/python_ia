from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>こんにちは</h1>')

def home(request):
    return render(request, 'myapp/home.html')

def mk(request):
    return render(request, 'myapp/mk.html')