from django.contrib import admin
from schedule.models import Schedule, Schedules

class SchedulesInline(admin.TabularInline):
    model = Schedules

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "date","availabe")
    list_display_links = ("id","doctor")
    inlines = [SchedulesInline]
    
admin.site.register(Schedule, ScheduleAdmin)
