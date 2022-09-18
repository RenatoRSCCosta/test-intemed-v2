from datetime import date, datetime
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from schedule.models import Schedule
from schedule.serializer import ScheduleSerializer


class ScheduleViewSet(GenericViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    
    def get_queryset(self):
        today = date.today()
        now = datetime.now().strftime('%H:%M')
        self.queryset = Schedule.objects.filter(Q(date__gt=today) | Q(date=today, schedules_schedule__hour__gte=now)).distinct()
        return self.queryset
    
    def list(self, *args, **kwargs):
        qs = self.get_queryset()
        serializer = ScheduleSerializer(qs, many=True)
        return Response(serializer.data)
