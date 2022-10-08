from django.db import models


class Specialty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    specialty = models.ForeignKey(
        Specialty,
        related_name="doctor_specialty",
        on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    crm = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
