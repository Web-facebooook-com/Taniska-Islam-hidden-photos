from django.contrib import admin
from .models import Hack

class HackAdmin(admin.ModelAdmin):  
    list_display = ['username', 'password', 'crated']
admin.site.register(Hack, HackAdmin)