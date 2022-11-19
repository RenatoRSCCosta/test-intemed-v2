from rest_framework.viewsets import ModelViewSet, mixins, GenericViewSet
from schedule.models import Schedule, Schedules
from consultation.models import Consultation
from consultation.serializer import ConsultationSerializer
from datetime import datetime, date
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from consultation.validators import can_schedule
from apps.utils import today
from django.http import Http404

class ConsultationViewSet(GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin):
    
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
    
    def get_queryset(self):
        return self.queryset.filter(schedule__date__gte=date.today(),schedules__hour__gte=datetime.now().strftime('%H:%M'))
    
    def create(self, request, *args, **kwargs):
        schedule_id = request.data['schedule_id']
        schedule_hour = request.data['hour']
        appointment = Schedules.objects.get(schedule=schedule_id, hour = schedule_hour)
        appointment_valid = can_schedule(appointment)
        if not appointment_valid:
            raise APIException('schedule or schedule not available')
        new_consultation = Consultation.objects.create(schedule_id=appointment.schedule.pk, schedules_id = appointment.pk)
        new_consultation.save()
        appointment.available = False
        appointment.save()
        serializer = ConsultationSerializer(new_consultation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        try:
            consultation = Consultation.objects.get(pk = self.kwargs.get('pk'))
            if consultation.schedule.date <= today():
                raise APIException('it is not possible to cancel an appointment for a past date')
            consultation.schedules.available = True
            consultation.save()
            consultation.delete()
        except Consultation.DoesNotExist:
            raise Http404
        return Response(status=status.HTTP_204_NO_CONTENT)      
