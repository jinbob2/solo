from django.contrib import admin

from .models import Bord
# Register your models here.

class BordAdmin(admin.ModelAdmin):
    list_display = ('title','user','check','timestamp')

admin.site.register(Bord, BordAdmin)
