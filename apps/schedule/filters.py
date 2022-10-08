from django_filters import rest_framework as filters
from schedule.models import Schedule


class ScheduleFilter(filters.FilterSet):
    doctor = filters.NumberFilter(lookup_expr='exact')
    crm = filters.CharFilter(field_name='doctor__crm', lookup_expr='exact')
    data_inicio = filters.DateFilter(field_name='date', lookup_expr='gte')
    data_final = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Schedule
        fields = ('doctor', 'doctor__crm', 'date')
