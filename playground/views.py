from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calc(a,b):
    print('hello')
    return a+b

def sayHello(request):
    x = 1
    y = 2 
    calc(x, y)
    return render(request, 'hello.html', {'name' : 'bilal'})
