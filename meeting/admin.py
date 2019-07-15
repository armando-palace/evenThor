from django.contrib import admin
from meeting.models import *

# Register your models here.
admin.site.register(Event)
admin.site.register(Presentation)
admin.site.register(Speaker)
admin.site.register(Assistant)
admin.site.register(Profile)
