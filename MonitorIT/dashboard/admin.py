from django.contrib import admin
from .models import Tasks
from .models import Execution
from django.contrib.auth.models import Group

admin.site.site_header = 'MonitorIT Dashboard'

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity')
    list_filter = ['category']

# Register your models here.
admin.site.register(Tasks,TaskAdmin)
admin.site.register(Execution)
#admin.site.unregister(Group)
