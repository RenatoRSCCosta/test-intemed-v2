from asyncore import read
from rest_framework import serializers
from consultation.models import Consultation
from schedule.serializer import ScheduleSerializer
from doctor.serializer import DoctorSerializer
from doctor.models import Doctor

class ConsultationSerializer(serializers.ModelSerializer):
    
    schedule_date = serializers.ReadOnlyField(source = 'schedule.date')
    schedules = serializers.CharField(read_only = True)
    doctor = serializers.SerializerMethodField('get_doctor', read_only=True)
    
    def get_doctor(self, consultation):
        queryset = Doctor.objects.get(id=consultation.schedule.doctor.id)
        return DoctorSerializer(instance = queryset).data
    
    class Meta:
        model = Consultation
        fields = (
            'id',
            'schedule_date',
            'schedules',
            'appointment_date',
            'doctor'
        )