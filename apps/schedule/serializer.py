from rest_framework import serializers
from schedule.models import Schedule, Schedules
from schedule.validators import schedules_available
from doctor.serializer import DoctorSerializer
        
class SchedulesSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        return str(instance.hour)[:5]
    
    class Meta:
        model = Schedules
        fields = (
            'hour',
        )
        
class ScheduleSerializer(serializers.ModelSerializer):

    schedules = serializers.SerializerMethodField('get_schedules')
    doctor = DoctorSerializer(many=False)
    
    def get_schedules(self, schedule):
        qs = schedules_available(schedule.id)
        serializer = SchedulesSerializer(instance=qs, many=True)
        return serializer.data
    
    class Meta:
        model = Schedule
        fields = (
            'id',
            'doctor', 
            'date',
            'schedules' 
        )