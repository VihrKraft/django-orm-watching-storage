from django.utils.timezone import localtime


SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SUSPICIOUS_TIME = 1


def get_duration(visit):
    time_now = localtime()
    entry_time = localtime(visit.entered_at)
    leaved_time = localtime(visit.leaved_at)
    if leaved_time:
        delta = leaved_time-entry_time
    else:
        delta = time_now-entry_time
    seconds = round(delta.total_seconds())
    return seconds


def format_duration(all_seconds):
    hours = all_seconds // SECONDS_PER_HOUR
    minutes = (all_seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
    seconds = all_seconds-(minutes*SECONDS_PER_MINUTE+hours*SECONDS_PER_HOUR)
    return f'{hours}ч {minutes}мин {seconds}сек'


def is_visit_long(visit_time, minutes=60):
    hours = (visit_time/SECONDS_PER_MINUTE)/minutes
    suspicion = hours>SUSPICIOUS_TIME
    return suspicion