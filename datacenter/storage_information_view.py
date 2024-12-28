from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from .utils import get_duration, format_duration, is_suspicious


def storage_information_view(request):
    open_visits = Visit.objects.filter(leaved_at=None)

    open_visits_data = []
    for visit in open_visits:
        duration = get_duration(visit)  # Получаем продолжительность
        formatted_duration = format_duration(duration)  # Форматируем продолжительность

        suspicious = is_suspicious(duration)  # Проверяем на подозрительность

        open_visits_data.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at.strftime('%d-%m-%Y %H:%M'),
            'duration': formatted_duration,
            'is_suspicious': suspicious,
        })

    context = {
        'open_visits': open_visits_data,
    }
    return render(request, 'storage_information.html', context)
