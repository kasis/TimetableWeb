from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from event.models import Events
from event.forms import AddEventForm
import datetime
import time
# Create your views here.

def add_event(request): 
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            e = Events(
                evt_name=cd['name'], 
                evt_place=cd['place'], 
                evt_start_time=cd['time_start'], 
                evt_end_time=cd['time_end'], 
                evt_date=cd['date'], 
                evt_note=cd['note']
            )
            e.save()
    else: 
        form = AddEventForm(
            initial={}
        )
    return render_to_response('add_event.html', {'form': form}, context_instance = RequestContext(request))
