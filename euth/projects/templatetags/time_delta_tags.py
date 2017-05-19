from django import template
from django.utils import timezone

register = template.Library()


@register.assignment_tag
def get_time_left(time):

    def seconds_in_units(seconds):
        unit_totals = {}

        unit_limits = [
                       ("week", 7 * 24 * 3600),
                       ("day", 24 * 3600),
                       ("hour", 3600),
                       ("minute", 60)
                        ]

        for unit_name, limit in unit_limits:
            if seconds >= limit:
                amount = int(float(seconds) / limit)
                unit_totals[unit_name] = amount
                seconds = seconds - (amount * limit)

        return unit_totals

    if isinstance(time, timezone.datetime):
        time_delta = time - timezone.now()
        seconds = time_delta.total_seconds()
        time_delta_dict = seconds_in_units(seconds)

        return time_delta_dict
