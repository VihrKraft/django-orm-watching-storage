from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from .tools import get_duration, format_duration


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)

    for visit in visits:
        entry_time = localtime(visit.entered_at)
        seconds = get_duration(visit)
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