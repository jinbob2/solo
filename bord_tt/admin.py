from django.contrib import admin

from .models import Bord
# Register your models here.

class BordAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')
    list_display = ['id','title','timestamp']
    search_fields = ['title']
    class Meta:
        model = Bord
admin.site.register(Bord, BordAdmin)