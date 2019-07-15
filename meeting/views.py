from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from meeting.models import Event, Presentation, Speaker, Assistant

from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Profile
from .forms import SignUpForm

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
  events = Event.objects.all()
  context = { 'events': events }
  return render(request, 'meeting/index.html', context)

def event_show(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  return render(request, 'meeting/show_event.html', { 'event': event })
  #return render (request, template_name = 'index.html')

class SignInView(LoginView):
  template_name = 'login.html'

@login_required
def home(request):
    user = request.user
    if user.has_perm('meeting.is_admin'):
      return redirect(reverse('home_admin'))
    elif user.has_perm('meeting.is_manager'):
      return redirect(reverse('home_manager'))
    elif user.has_perm('meeting.is_agent'):
      return redirect(reverse('home_agent'))
    else:
      return render (request, template_name = 'index.html')

@permission_required('meeting.is_admin')
def home_admin(request):
  return render(request, template_name='home_admin.html')

@permission_required('meeting.is_manager')
def home_manager(request):
  return render(request, template_name='home_manager.html')

@permission_required('meeting.is_agent')
def home_agent(request):
  return render(request, template_name='home_agent.html')




class SignOutView(LogoutView):
  pass
