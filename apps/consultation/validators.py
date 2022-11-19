from schedule.models import Schedules
from apps.utils import today, now

def can_schedule(appointment):
    date = today()
    hour = now()
    print(appointment.hour)
    if appointment.schedule.date >= date and appointment.hour.strftime('%H:%M:%S') >= hour:
        return True
    return False