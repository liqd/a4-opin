from django import template
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.simple_tag
def get_time_left(time):

    def seconds_in_units(seconds):
        unit_totals = []

        unit_limits = [
            ([_('week'), _('weeks')], 7 * 24 * 3600),
            ([_('day'), _('days')], 24 * 3600),
            ([_('hour'), _('hours')], 3600),
            ([_('minute'), _('minutes')], 60),
            ([_('second'), _('seconds')], 1)
        ]

        for unit_name, limit in unit_limits:
            if seconds >= limit:
                amount = int(float(seconds) / limit)
                if amount > 1:
                    unit_totals.append((unit_name[1], amount))
                else:
                    unit_totals.append((unit_name[0], amount))
                seconds = seconds - (amount * limit)

        return unit_totals

    if time:
        time_delta = time - timezone.now()
        seconds = time_delta.total_seconds()
        time_delta_list = seconds_in_units(seconds)
        time_delta_str = (_('and') +
                          (' ')).join([(str(val[1]) + ' ' +
                                        str(val[0]) + ' ')
                                      for val in time_delta_list[:2]])

        return time_delta_str
