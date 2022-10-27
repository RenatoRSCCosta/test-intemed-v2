from asyncore import read
from rest_framework import serializers
from schedule.models import Schedule, Schedules
from schedule.validators import schedules_available
from doctor.serializer import DoctorSerializer
from datetime import datetime, date
from django.db.models import Q


class SchedulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedules
        fields = (
            'hour',
        )

    def to_representation(self, instance):
        return str(instance.hour)[:5]


class ScheduleSerializer(serializers.ModelSerializer):

    schedules = serializers.SerializerMethodField(
        'get_valid_schedules', read_only=True)
    doctor = DoctorSerializer(many=False, read_only=True)

    class Meta:
        model = Schedule
        fields = (
            'id',
            'doctor',
            'date',
            'schedules'
        )

    def get_valid_schedules(self, schedule_id):
        qs = Schedules.objects.filter(Q(schedule_id=schedule_id, schedule__date=date.today(),hour__gte=datetime.now().strftime('%H:%M'), available=True)
        | Q(schedule_id=schedule_id, schedule__date__gt=date.today(), available=True))
        serializer = SchedulesSerializer(instance=qs, many=True)
        return serializer.data
