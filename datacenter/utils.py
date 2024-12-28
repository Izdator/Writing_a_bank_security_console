from django.utils import timezone


def get_duration(visit):
    if visit.leaved_at:
        duration = (visit.leaved_at - visit.entered_at).total_seconds()
    else:
        duration = (timezone.now() - visit.entered_at).total_seconds()
    return duration


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    formatted_duration = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
    return formatted_duration


def is_suspicious(duration):
    return duration > 3600
