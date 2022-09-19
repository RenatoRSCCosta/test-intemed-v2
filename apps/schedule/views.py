from datetime import date, datetime
from django.db.models import Q
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from schedule.models import Schedule, Schedules
from schedule.serializer import ScheduleSerializer, SchedulesSerializer
#from schedule.filters import ScheduleFilter


class ScheduleViewSet(GenericViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    #filter_backends = (DjangoFilterBackend,)
    #filterset_fields = ('doctor',)
    #filterset_class = ScheduleFilter
    
    def get_queryset(self):
        today = date.today()
        now = datetime.now().strftime('%H:%M')
        return self.queryset.filter(date__gte=today, schedules_schedule__hour__gte=now)
    
    def list(self, *args, **kwargs):
        qs = self.get_queryset()
        serializer = ScheduleSerializer(qs, many=True)
        return Response(serializer.data)
