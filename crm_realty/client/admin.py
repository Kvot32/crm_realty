from django.contrib import admin
from .models import Client, Application, Feedback, Deal

admin.site.register(Client)
admin.site.register(Application)
admin.site.register(Feedback)
admin.site.register(Deal)
