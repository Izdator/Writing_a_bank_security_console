from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from .utils import calculate_and_format_duration, is_suspicious


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = []

    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        duration, formatted_duration = calculate_and_format_duration(visit)
        suspicious = is_suspicious(duration)

        this_passcard_visits.append({
            'entered_at': visit.entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': formatted_duration,
            'is_strange': suspicious
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
