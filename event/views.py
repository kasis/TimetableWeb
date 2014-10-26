from django.shortcuts import render_to_response
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
            e = Events(evt_name='name', evt_place='place', evt_start_time='time_start', evt_end_time='time_end', evt_date='date', evt_note='note')
            e.save()
            return HttpResponseRedirect('/add_event/thanks/')
    else: 
        form = AddEventForm(
            initial={}
        )
    return render_to_response('add_event.html', {'form': form})
