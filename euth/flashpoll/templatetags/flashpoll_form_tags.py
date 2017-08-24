import datetime
import json

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def print_timestamp(timestamp):
    try:
        # assume, that timestamp is given in seconds with decimal point
        ts = float(str(timestamp))
    except ValueError:
        return None
    return str(datetime.datetime.fromtimestamp(ts))


@register.filter
def get_simplejson(modelobject):
    return json.dumps(modelobject)


@register.filter(name='get_poll_from_string')
def get_poll_from_string(poll):
    return json.loads(poll)


@register.filter(name='get_description_errors')
def get_description_errors(errors):
    qerrors = 0
    geoerrors = 0
    for line in errors:
        if "question" in line:
            qerrors = qerrors + 1

        if "geofenceLocation" in line:
            geoerrors = geoerrors + 1

    return len(errors) - (qerrors + geoerrors)


@register.filter(name='get_questions_errors')
def get_questions_errors(errors):
    qerrors = 0
    for line in errors:
        if "question" in line:
            qerrors = qerrors + 1

    return qerrors


@register.filter(name='get_poll_questions')
def get_poll_questions(poll):
    polljson = json.loads(poll)
    pollout = json.dumps(polljson['questions'])
    return pollout


@register.filter(name='get_answersjson')
def get_answersjson(questions, field_name):
    orderid = int(field_name.split("_")[1])
    answers = questions[orderid-1]['answers']
    return json.dumps(answers)


@register.filter(name='is_lastanswer')
def is_lastanswer(questions, field_name):
    qorderid = int(field_name.split("_")[1])
    qcorderid = int(field_name.split("_")[3])
    answers = questions[qorderid-1]['answers']
    return (len(answers) == qcorderid)


@register.filter(name='is_lastquestion')
def is_lastquestion(questions, field_name):
    orderid = int(field_name.split("_")[1])
    return (len(questions) == orderid)


@register.filter(name='is_firstanswer')
def is_firstanswer(field_name):
    qcorderid = int(field_name.split("_")[3])
    return (1 == qcorderid)


@register.filter(name='is_firstquestion')
def is_firstquestion(field_name):
    orderid = int(field_name.split("_")[1])
    return (1 == orderid)


@register.filter(name='is_openquestion')
def is_openquestion(questions, field_name):
    orderid = int(field_name.split("_")[1])
    type = questions[orderid-1]['questionType']
    return (type[0] == 'FREETEXT' or type == 'FREETEXT')


@register.filter(name='get_field_endswith')
def get_field_endswith(field_name, end_name):
    if end_name in field_name:
        return True
    return False


@register.filter(name='get_question_orderid')
def get_question_orderid(field_name):
    # question_9_questionText
    orderid = field_name.split("_")[1]
    return orderid


@register.filter(name='get_answer_orderid')
def get_answer_orderid(field_name):
    # question_9_choice_5_answerText
    orderid = field_name.split("_")[3]
    return orderid


@register.simple_tag
def api_key():
    try:
        return settings.GOOGLE_API_KEY
    except AttributeError:
        return ''
