from datacenter.models import Passcard, Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .tools import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        seconds = get_duration(visit)

        duration = format_duration(seconds)

        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': duration,
            'is_strange': is_visit_long(seconds),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
