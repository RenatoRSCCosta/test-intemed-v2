from django.contrib import admin
from doctor.models import Doctor, Specialty

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id","name", "crm", "email",)
    list_display_links = ("id","name",)

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("id","name",)
    list_display_links = ("id","name",)
    
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
    