from django.contrib import admin
from meeting.models import Event, Speaker, Presentation, Assistant

# Register your models here.
admin.site.register(Event)
admin.site.register(Presentation)
admin.site.register(Speaker)
admin.site.register(Assistant)
