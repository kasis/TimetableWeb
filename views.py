from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
    hello = 'hello world'
    return render_to_response('hello.html', {'hello': hello})

def main(request):
    return render_to_response('main.html')



