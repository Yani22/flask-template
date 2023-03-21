from datetime import datetime, timezone, timedelta

# values here will be added based on UTC
# Ex. PHT --> UTC + 8
timezones = {
    'PHT' : 8
}

# def get_current_datetime():
def current_datetime(tz='PHT', raise_exception=False):  # sourcery skip: raise-specific-error
    # raise error if raise_exception is True
    if raise_exception and (tz not in timezones):
        raise Exception('TimeZone not found')

    # use Philippines Time by default
    else:
        tz = 'PHT'

    # NOTE: tzinfo is removed because of db insertion issues
    return (datetime.now(timezone.utc) + timedelta(hours=timezones[tz])).replace(tzinfo=None)

# compute how many months elapsed between start date and end date 
# NOTE: days are also included in the computation
def compute_monthsary(start_date, end_date):
    months = end_date.month - start_date.month + 12*(end_date.year - start_date.year)

    if start_date.day > end_date.day:
        months -= 1

    return months

# compute how many years elapsed between start date and end date
def compute_anniversary(start_date, end_date):
    pass