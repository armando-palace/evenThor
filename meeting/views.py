from django.shortcuts import render
from django.http import HttpResponse
from meeting.models import Event, Presentation, Speaker, Assistant

# Create your views here.
def index(request):
  my_dictionary = {'insert_me': 'Hello!'}
  return render(request, 'meeting/index.html', context=my_dictionary)
