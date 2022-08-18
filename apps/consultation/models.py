from re import M
from django.db import models
from schedule.models import Schedule, Schedules

class Consultation(models.Model):
    schedule_id = models.ForeignKey(Schedule, related_name="Schedule", on_delete=models.CASCADE)
    schedules_id = models.ForeignKey(Schedules, related_name="Schedules", on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consulta no horario de {self.schedules_id.hour} no dia {self.schedule_id.date} https://github.com/RenatoRSCCosta/test-intemed-v2.git"
