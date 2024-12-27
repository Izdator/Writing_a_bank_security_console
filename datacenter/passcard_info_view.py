from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def calculate_and_format_duration(visit):
    if visit.leaved_at:
        duration = (visit.leaved_at - visit.entered_at).total_seconds() / 60
    else:
        duration = (timezone.now() - visit.entered_at).total_seconds() / 60

    formatted_duration = "{:02}:{:02}".format(int(duration // 60), int(duration % 60))

    return duration, formatted_duration


def is_suspicious(duration):
    return duration > 60


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
