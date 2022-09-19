from django.db import models
from doctor.models import Doctor

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="schedule_doctor", on_delete=models.CASCADE)
    date = models.DateField()
    availabe = models.BooleanField(default=True)

    def __str__(self):
        return f"Agenda de {self.doctor} para data de {self.date}"
    
    class Meta:
        ordering = ["date"]
    
class Schedules(models.Model):
    schedule = models.ForeignKey(Schedule, related_name="schedules_schedule", on_delete=models.CASCADE)
    hour = models.TimeField()
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.hour)[:5]
    
    class Meta:
        ordering = ["hour"]
        unique_together = ("schedule", "hour")
        