from django.db import models
from schedule.models import Schedule, Schedules


class Consultation(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        related_name="consultation_schedule",
        on_delete=models.CASCADE)
    schedules = models.ForeignKey(
        Schedules,
        related_name="consultation_schedules",
        on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consulta no horario de {self.schedules.hour} no dia {self.schedule.date}"

    class Meta:
        unique_together = ("schedule", "schedules")
