from django.contrib import admin
from .models import *

class contactlistAdmin(admin.ModelAdmin):
    list_display = ('name','Phone_number')
# Register your models here.

admin.site.register(contactlist,contactlistAdmin)
