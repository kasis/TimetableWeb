from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from event.models import Event
from event.forms import AddEventForm
import datetime
import time
# Create your views here.
               
@login_required
def day_events(request, year, month, day):
    try:
        year = int(year)
        month = int(month)
        day = int(day)
    except:
        raise Http404() 
    now = datetime.date(year, month, day)
    timedelta1 = datetime.timedelta(days=1)
    day_inc = now + timedelta1
    day_inc = day_inc.strftime('%Y/%m/%d')
    timedelta2 = datetime.timedelta(days=-1)
    day_dec = now + timedelta2
    day_dec = day_dec.strftime('%Y/%m/%d')
    user_events = Event.objects.filter(owner = request.user)
    user_events = user_events.filter(evt_date = now )
    now = now.strftime("%a, %d. %b %Y")
    now_link = datetime.datetime.now().strftime('%Y/%m/%d')
    return render_to_response('day_events.html', {
            'user_events': user_events,
            'date': now,
            'day_dec': day_dec,
            'day_inc': day_inc,
            'now_link': now_link
            },
            context_instance = RequestContext(request)
        )

@login_required
def add_event(request): 
    if request.method == 'POST':
        e = Event(
                evt_name=request.POST['name'], 
                evt_place=request.POST['place'], 
                evt_start_time=request.POST['start_time'], 
                evt_end_time=request.POST['end_time'], 
                evt_date=request.POST['date'], 
                evt_note=request.POST['note'],
                owner=request.user)
        e.save()
        return HttpResponseRedirect('/')
    return render_to_response('add_event.html', context_instance = RequestContext(request))

@login_required
def active_event(request, cur_id):
    event = Event.objects.get(id = cur_id)
    if request.user == event.owner:    
        if request.method == 'POST':    
            event.evt_note = request.POST['note']
            event.save()
            return HttpResponseRedirect('/')
        return render_to_response('active_event.html', {
            'event': event,
            },
            context_instance = RequestContext(request)
            )
    else:
        raise Http404()
