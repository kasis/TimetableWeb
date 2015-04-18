from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from event.models import Event
import datetime
# Create your views here.

@login_required
def day_events(request, day_iter):
    try:
        day_iter = int(day_iter)
    except:
        raise Http404()
    day_inc = day_iter + 1
    day_dec = day_iter - 1
    now = datetime.datetime.now() + datetime.timedelta(days=day_iter)
    user_events = Event.objects.filter(owner=request.user)
    user_events = user_events.filter(evt_date=now)
    now = now.strftime("%a, %d. %b %Y")
    return render_to_response('day_events.html', {
        'user_events': user_events,
        'date': now,
        'day_dec': day_dec,
        'day_inc': day_inc,
    },
        context_instance=RequestContext(request)
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
    return render_to_response('add_event.html', context_instance=RequestContext(request))


@login_required
def active_event(request, cur_id):
    event = Event.objects.get(id=cur_id)
    if request.user == event.owner:
        if request.method == 'POST':
            event.evt_note = request.POST['note']
            event.save()
            return HttpResponseRedirect('/')
        return render_to_response('active_event.html', {
            'event': event,
        },
            context_instance=RequestContext(request)
        )
    else:
        raise Http404()
