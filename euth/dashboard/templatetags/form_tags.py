from django import template
import datetime
import json
register = template.Library()


def print_timestamp(timestamp):
    try:
        #assume, that timestamp is given in seconds with decimal point
        ts = float(timestamp)
    except ValueError:
        return None
    print("timestamp: "+str(timestamp)+" date: "+str(datetime.datetime.fromtimestamp(ts)))
    return str(datetime.datetime.fromtimestamp(ts))

register.filter(print_timestamp)



def get_simplejson(modelobject):
    return json.dumps(modelobject)

register.filter(get_simplejson)


@register.assignment_tag
def get_checkbox_label(form, fieldname):
    return form.get_checkbox_label(fieldname)
