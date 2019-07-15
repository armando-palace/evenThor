from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from meeting.models import Event, Presentation, Speaker, Assistant

# Create your views here.
def index(request):
  events = Event.objects.all()
  context = { 'events': events }
  return render(request, 'meeting/index.html', context)

def event_show(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  return render(request, 'meeting/show_event.html', { 'event': event })