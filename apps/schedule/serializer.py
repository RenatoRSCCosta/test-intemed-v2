from rest_framework import serializers
from schedule.models import Schedule, Schedules
from doctor.serializer import DoctorSerializer
        
class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = (
            'hour',
        )
        
class ScheduleSerializer(serializers.ModelSerializer):
    Schedule = serializers.StringRelatedField(many=True)
    doctor = DoctorSerializer(many=False)
    class Meta:
        model = Schedule
        fields = (
            'id',
            'doctor', 
            'date',
            'Schedule' 
        )