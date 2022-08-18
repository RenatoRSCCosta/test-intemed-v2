from operator import mod
from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    specialty_id = models.ForeignKey(Specialty, related_name="Specialty", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    crm = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
