from django.shortcuts import render_to_response
# Create your views here.

def add_event(request):
    return render_to_response('add_event.html')
