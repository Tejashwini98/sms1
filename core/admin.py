from django.contrib import admin

# Register your models here.
from .models import Application,Scheme
admin.site.register(Application)
admin.site.register(Scheme)