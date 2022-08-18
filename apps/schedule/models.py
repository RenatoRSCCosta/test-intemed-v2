from sched import scheduler
from django.db import models
from doctor.models import Doctor

class Schedule(models.Model):
    doctor_id = models.ForeignKey(Doctor, related_name="Doctor", on_delete=models.CASCADE)
    date = models.DateField()
    availabe = models.BooleanField(default=True)

    def __str__(self):
        return f"Agenda de {self.doctor_id} para data de {self.date}"
    
class Schedules(models.Model):
    schedule_id = models.ForeignKey(Schedule, related_name="Schedule", on_delete=models.CASCADE)
    hour = models.TimeField()
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"horario {self.hour} para agenda na data de {self.schedule_id.date}"