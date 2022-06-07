from calendar import monthrange
from datetime import datetime


def get_assigned_date(date: datetime):
    if (date.weekday() <= 4 and date.hour >= 22) or (date.weekday() > 4 and date.hour >= 18):
        if date.day == monthrange(date.year, date.month)[1]:
            return date.day, date.month + 1
        else:
            return date.day + 1, date.month
    return 999, 9999