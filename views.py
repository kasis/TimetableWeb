from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime
import time
import django.forms


def hello(request):
    hello = 'hello world'
    return render_to_response('hello.html', {'hello': hello})

def main(request):
    now = datetime.datetime.now().strftime("%a, %d. %b %Y")
    now_link = datetime.datetime.now().strftime('%Y/%m/%d')
    return render_to_response('main.html', {
        'date': now,
        'now_link': now_link
        },
	context_instance = RequestContext(request)
	)

def later(request):
    return HttpResponse("nope")

def registration(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']).exists():
            #TODO: pass error to template
            raise django.forms.ValidationError("This email is already used")
        if User.objects.filter(username=request.POST['username']).exists():
            #TODO: pass error to template
            raise django.forms.ValidationError("This user name is already used")
        user = User.objects.create_user(
                    request.POST['username'],
                    request.POST['email'],
                    request.POST['password']
                )
        return HttpResponseRedirect('/accounts/login/')
    return render_to_response("accounts/register.html", {
                'username': request.POST.get('username', ''),
                'email': request.POST.get('email', ''),
                'password': request.POST.get('password', ''),
            },
            context_instance = RequestContext(request)
            )

@login_required
def my_profile(request):
    user = request.user
    return render_to_response("login.html", { "user": user }, context_instance = RequestContext( request ) )

