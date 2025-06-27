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
    all_minutes = round(delta.total_seconds()/60)
    return all_minutes



def format_duration(all_minutes):
    hours = all_minutes // 60
    minutes = all_minutes-hours*60
    return f'{hours}ч {minutes}мин'


def is_visit_long(all_minutes):
    all_hours = all_minutes / 60
    if all_hours>1:
        return True
    else:
        return False


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        all_minutes = get_duration(visit)

        duration = format_duration(all_minutes)

        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_visit_long(all_minutes),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
