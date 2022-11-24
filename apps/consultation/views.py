from rest_framework.viewsets import mixins, GenericViewSet
from consultation.models import Consultation
from consultation.serializer import ConsultationListSerializer, ConsultationCreateSerializer
from datetime import datetime, date
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from apps.utils import today
from django.http import Http404

class ConsultationViewSet(GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          mixins.DestroyModelMixin):
    
    queryset = Consultation.objects.all()
    serializer_class = ConsultationListSerializer
    serializer_action_classes = {
        'create':ConsultationCreateSerializer,
    }
    
    def get_serializer_class(self, *args, **kwargs):
        """Instantiate the list of serializers per action from class attribute (must be defined)."""
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(ConsultationViewSet, self).get_serializer_class()
    
    def get_queryset(self):
        return self.queryset.filter(schedule__date__gte=date.today(),schedules__hour__gte=datetime.now().strftime('%H:%M'))
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()
        consultation = serializer(data=request.data)
        if consultation.is_valid(raise_exception=True):
            appointment = consultation.save()
            result = ConsultationListSerializer(appointment)
            print(result.data)
            response = Response(result.data, status=status.HTTP_201_CREATED)
            return response
    
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
