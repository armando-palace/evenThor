from django.urls import path
from . import views

app_name = 'meeting'
urlpatterns = [
  # /meeting
  path('', views.index, name='index'),
  # /meeting/events/:event_id
  path('events/<int:event_id>/', views.show_event, name='show_event')
  path('events/new', views.new_event, name='new_event')
]
