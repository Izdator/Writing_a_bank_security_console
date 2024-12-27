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
