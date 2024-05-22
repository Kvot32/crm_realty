from django.contrib import admin
from .models import Client, Application, Feedback

admin.site.register(Client)
admin.site.register(Application)
admin.site.register(Feedback)
