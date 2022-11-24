from datetime import date, datetime
from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
from schedule.models import Schedule
from schedule.serializer import ScheduleSerializer
from schedule.filters import ScheduleFilter


class ScheduleViewSet(GenericViewSet,
                      mixins.ListModelMixin):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ScheduleFilter

    def get_queryset(self):
        return self.queryset.filter(Q(date__gte=date.today(),
                                    schedules_schedule__hour__gte=datetime.now().strftime('%H:%M'))
                                    | Q(date__gt=date.today())).distinct()
   
    def list(self, request, *args,):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = ScheduleSerializer(filter_queryset, many=True)
        return Response(serializer.data)
    
