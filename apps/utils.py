from datetime import datetime, date


def today():
    return date.today()

def now():
    return datetime.now().strftime('%H:%M:%S')