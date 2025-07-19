from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def get_duration(visit):
    time_now = localtime()
    entry_time = localtime(visit.entered_at)
    leaved_time = localtime(visit.leaved_at)
    if leaved_time:
        delta = leaved_time-entry_time
    else:
        delta = time_now-entry_time
    minutes = round(delta.total_seconds()/60)
    return minutes



def format_duration(minutes):
    hours = minutes // 60
    remaining_minutes = minutes-hours*60
    return f'{hours}ч {remaining_minutes}мин'


def is_visit_long(visit_time, minutes=60):
    hours = visit_time/minutes
    if hours>1:
        return True
    else:
        return False


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        minutes = get_duration(visit)

        duration = format_duration(minutes)

        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_visit_long(minutes),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
