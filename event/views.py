from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from event.models import Event
from event.forms import AddEventForm
import datetime
import time
# Create your views here.

def main(request):
    user_events = Event.objects.filter(owner = request.user)
    now = datetime.datetime.now().strftime("%a, %d. %b")
    return render_to_response('main.html', {
            'date': now,
            'user_events': user_events
            },
            context_instance =
            RequestContext(request)
        ) 
               
@login_required
def add_event(request): 
    errors = []
    if request.method == 'POST':
        if not request.POST.get('name', ''):
            errors.append('Enter an eventname.')
        if not request.POST.get('place', ''):
            errors.append('Enter an eventplace.')
        if not request.POST.get('start_time', ''):
            errors.append('Enter a start time.')
        if not request.POST.get('end_time', ''):
            errors.append('Enter an end time.')
        if not request.POST.get('date', ''):
            errors.append('Enter a date.')
        if not errors:
            e = Event(
                evt_name=request.POST['name'], 
                evt_place=request.POST['place'], 
                evt_start_time=request.POST['start_time'], 
                evt_end_time=request.POST['end_time'], 
                evt_date=request.POST['date'], 
                evt_note=request.POST['note'],
                owner=request.user
            )
            e.save()
            return HttpResponseRedirect('/')
    return render_to_response('add_event.html', {'errors': errors}, context_instance = RequestContext(request))

@login_required
def active_event(request, cur_id):
    event = Event.objects.filter(id = cur_id)
    return render_to_response('active_event.html', {'event': event})
