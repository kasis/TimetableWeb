from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import time

def hello(request):
    hello = 'hello world'
    return render_to_response('hello.html', {'hello': hello})

def main(request):
    mnth = ['Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun' , 'Jul', 'Aug' , 'Sept' , 'Oct' , 'Nov' , 'Dec'] 
    wdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    now = datetime.datetime.now()
    now_mnth = mnth[now.month - 1]
    n_weekday = wdays[time.localtime().tm_wday]
    return render_to_response('main.html', {'date_day': now.day, 'date_month': now_mnth, 'date_weekday': n_weekday })



