from datetime import date
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from schedule.models import Schedule
from schedule.serializer import ScheduleSerializer
from schedule.filters import ScheduleFilter


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    filterset_class = ScheduleFilter

    def get_queryset(self):
        return self.queryset.filter(date__gte=date.today())

    # def list(self, *args, **kwargs):
    #    queryset = self.get_queryset()
    #    serializer = ScheduleSerializer(queryset, many=True)
    #    return Response(serializer.data)
