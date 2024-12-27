from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)

    visits_data = []
    for visit in non_closed_visits:
        visits_data.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': str(timezone.now() - visit.entered_at),
        })

    context = {
        'non_closed_visits': visits_data,
    }
    return render(request, 'storage_information.html', context)

