from django.contrib import admin
from .models import *
# Register your models here.

class SelectWorker(admin.ModelAdmin):
    search_fields=['name']
    list_display =['name','phone_number']

class SelectUnit(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name','worker']

class Selectvisit(admin.ModelAdmin):
    search_fields=['unit__name','unit__worker__name']
    list_display=['date_time','unit','latitude','longitude']
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Worker, SelectWorker)
admin.site.register(Unit, SelectUnit)
admin.site.register(Visit, Selectvisit)