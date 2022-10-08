from django.forms import ModelForm
from schedule.models import Schedule
from schedule.validators import *


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

    def clean(self):
        schedule_id = self.instance.pk
        schedule_date = self.cleaned_data.get('date')
        doctor = self.cleaned_data.get('doctor')
        errors_list = {}
        doctor_with_schedule(doctor, schedule_date, schedule_id, errors_list)
        retroactive_day(schedule_date, errors_list)
        if errors_list is not None:
            for error in errors_list:
                error_message = errors_list[error]
                self.add_error(error, error_message)
        return self.cleaned_data
