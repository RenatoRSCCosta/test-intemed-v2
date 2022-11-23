from asyncore import read
from rest_framework import serializers
from consultation.models import Consultation
from schedule.models import Schedules
from doctor.serializer import DoctorSerializer
from doctor.models import Doctor
from apps.utils import *
from django.db import IntegrityError


class ConsultationCreateSerializer(serializers.ModelSerializer):
       
    schedule_id = serializers.IntegerField()
    hour = serializers.CharField()

    def validate(self, data):
        try:
            appointment = Schedules.objects.get(schedule=data['schedule_id'], hour = data['hour'])
        except Schedules.DoesNotExist:
            raise serializers.ValidationError("It was not possible to book your appointment, please check the schedule or hour")
        if appointment.schedule.date < today() and appointment.hour.strftime('%H:%M') <= now():
            raise serializers.ValidationError("it is not possible to make a schedule for a retroactive day or time")
        return data
    
    def create(self, validated_data):
        try:
            appointment = Schedules.objects.get(schedule_id = validated_data["schedule_id"], hour = validated_data['hour'])
            return Consultation.objects.create(schedule_id=appointment.schedule.pk,schedules_id=appointment.pk)
        except IntegrityError as e:
            if 'unique constraint' in e.args:
                raise serializers.ValidationError("it is not possible to schedule an appointment already scheduled")
        
    
    class Meta:
        model = Consultation
        fields = (
            'schedule_id',
            'hour'
        )

class ConsultationListSerializer(serializers.ModelSerializer):
    
    schedule_date = serializers.ReadOnlyField(source = 'schedule.date')
    hour = serializers.CharField(read_only = True, source = 'schedules.hour')
    doctor = serializers.SerializerMethodField('get_doctor', read_only=True)
    
    def get_doctor(self, consultation):
        queryset = Doctor.objects.get(id=consultation.schedule.doctor.id)
        return DoctorSerializer(instance = queryset).data
    
    class Meta:
        model = Consultation
        fields = (
            'id',
            'hour',
            'schedule_date',
            'appointment_date',
            'doctor'
        )