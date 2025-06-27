from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(time_now, entry_time):
    delta = time_now-entry_time
    seconds = round(delta.total_seconds())
    return seconds


def format_duration(all_seconds):
    hours = all_seconds // 3600
    minutes = (all_seconds % 3600) // 60
    seconds = all_seconds-(minutes*60+hours*3600)
    return f'{hours}ч {minutes}мин {seconds}сек'


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)
    time_now = localtime()

    for visit in visits:
        entry_time = localtime(visit.entered_at)
        seconds = get_duration(time_now, entry_time)
        duration = format_duration(seconds)
        visitor_name = visit.passcard

        non_closed_visits.append({
            'who_entered': visitor_name,
            'entered_at': entry_time,
            'duration': duration,
        })
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)