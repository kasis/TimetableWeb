from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import time

def hello(request):
    hello = 'hello world'
    return render_to_response('hello.html', {'hello': hello})

def main(request):
    now = datetime.datetime.now().strftime("%a, %d. %b")
    return render_to_response('main.html', {'date': now })


