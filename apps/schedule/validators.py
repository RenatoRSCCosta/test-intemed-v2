from datetime import date
from schedule.models import Schedule

def retroactive_day(schedule_date, errors_list):
    """validates if the schedule is being created for a retroactive day"""
    today = date.today()
    if schedule_date < today:
        errors_list['date'] = "Nao e possivel criar agenda em dias retroativos"


def doctor_with_schedule(doctor, schedule_date,schedule_id, errors_list):
    """validates if the doctor already has an schedule for the one in which the agenda is being created"""  
    if schedule_id:
        schedule = Schedule.objects.get(pk=schedule_id)
    if schedule_id is None or schedule.date != schedule_date:
         doctor_schedules = Schedule.objects.filter(doctor=doctor, date=schedule_date)
         if doctor_schedules:
             errors_list['doctor'] = "Não é possivel criar mais de uma agenda para o mesmo medico no mesmo dia"
             
def can_edit_schedules():
    """validates if it is possible to edit a timetable"""
    pass

def schedule_valid():
    """validates schedule and schedules according to business rules"""
    pass