from rest_framework.viewsets import ModelViewSet
from schedule.models import Schedule, Schedules
from consultation.models import Consultation
from consultation.serializer import ConsultationSerializer
from datetime import datetime, date
from rest_framework.response import Response

class ConsultationViewSet(ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    
    def get_queryset(self):
        return self.queryset.filter(schedule__date__gte=date.today(),schedules__hour__gte=datetime.now().strftime('%H:%M'))
    
    def create(self, request, *args, **kwargs):
        data = request.data
        schedule_id = data['schedule_id']
        schedule_hour = data['hour']
        appointment = Schedules.objects.get(schedule=schedule_id, hour = schedule_hour)
        new_consultation = Consultation.objects.create(schedule_id=appointment.schedule.pk, schedules_id = appointment.pk)
        new_consultation.save()
        serializer = ConsultationSerializer(new_consultation)
        return Response(serializer.data)       
