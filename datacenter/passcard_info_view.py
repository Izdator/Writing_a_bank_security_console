from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def get_duration(visit):
    if visit.leaved_at:
        return (visit.leaved_at - visit.entered_at).total_seconds() / 60
    else:
        return (timezone.now() - visit.entered_at).total_seconds() / 60


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    this_passcard_visits = []

    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        duration = get_duration(visit)
        is_strange = duration > 60

        this_passcard_visits.append({
            'entered_at': visit.entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': "{:02}:{:02}".format(int(duration // 60), int(duration % 60)),
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)