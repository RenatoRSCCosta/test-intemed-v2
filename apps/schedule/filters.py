from django_filters import rest_framework as filters
from schedule.models import Schedule


class ScheduleFilter(filters.FilterSet):
    doctor = filters.NumberFilter(field_name='doctor', method='filter_doctor')
    crm = filters.CharFilter(field_name='doctor__crm', method='filter_crm')
    start_date = filters.DateFilter(field_name='date', method='filter_date')
    end_date = filters.DateFilter(field_name='date', method='filter_date')

    def filter_doctor(self, queryset, name, value):
        if value:
            doctors = self.request.query_params.getlist('doctor')
            return queryset.filter(doctor__in=doctors)
        return queryset
    
    def filter_crm(self, queryset, name, value):
        if value:
            crms = self.request.query_params.getlist('crm')
            return queryset.filter(doctor__crm__in=crms)
        return queryset
    
    def filter_date(self, queryset, name, value):
        if value:
            start_date = self.request.query_params.get('start_date')
            end_date = self.request.query_params.get('end_date')
            return queryset.filter(date__range=(start_date, end_date))
        return queryset
    
    class Meta:
        model = Schedule
        fields = ('doctor', 'doctor__crm', 'date')
