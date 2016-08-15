from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core import urlresolvers
from django.db.models import ForeignKey
from django.template import Context

from euth.contrib import emails


def send_email_to_moderators(request, report):

    obj = report.content_object

    if obj:
        name = obj._meta.verbose_name.title()

        try:
            admin_url = urlresolvers.reverse("admin:%s_%s_change" %
                                             (obj._meta.app_label,
                                              obj._meta.model_name),
                                             args=(obj.pk,))
            admin_url = request.build_absolute_uri(
                admin_url)
        except:
            admin_url = ''

        moderators = get_user_model().objects.filter(is_superuser=True)

        recievers = [
            u.email for u in moderators]

        context = Context({
            'site': Site.objects.get_current(),
            'name': name,
            'admin_url': admin_url,
            'description': report.description
        })

        emails.send_email_with_template(
            recievers, 'report_moderators', context)


def send_email_to_creator(request, report):

    obj = report.content_object
    if obj:
        creator_field = get_creator_field(obj)
        if creator_field:
            creator = getattr(obj, creator_field)
            recievers = [creator.email]
            name = obj._meta.verbose_name.title()

            context = Context({
                'site': Site.objects.get_current(),
                'name': name,
                'description': report.description
            })

            emails.send_email_with_template(
                recievers, 'report_creator', context)


def get_creator_field(obj):
    fields = obj._meta.fields

    for f in fields:
        field_object, model, direct, m2m = obj._meta.get_field_by_name(f.name)
        if not m2m and direct and isinstance(field_object, ForeignKey):
            if field_object.rel.to == get_user_model():
                return f.name

    return None
