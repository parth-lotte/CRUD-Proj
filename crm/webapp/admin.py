from django.contrib import admin

# Register your models here.
#  remember class name for model reg 

from . models import Record

admin.site.register(Record)
