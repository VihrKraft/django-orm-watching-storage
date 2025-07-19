from django.utils.timezone import localtime


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
    hours = all_seconds // 3600
    minutes = (all_seconds % 3600) // 60
    seconds = all_seconds-(minutes*60+hours*3600)
    return f'{hours}ч {minutes}мин {seconds}сек'


def is_visit_long(visit_time, minutes=60):
    hours = (visit_time/60)/minutes
    suspicion = hours>1
    return suspicion