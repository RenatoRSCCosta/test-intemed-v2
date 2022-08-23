from django.contrib import admin
from schedule.models import Schedule, Schedules

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor_id", "date","availabe")
    list_display_links = ("id","doctor_id")
    
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ("id", "hour","availabe")
    list_display_links = ("id","hour")
    
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Schedules, SchedulesAdmin)
