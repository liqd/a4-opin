from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core import urlresolvers
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template import Context

from euth.contrib import emails

from .models import Report


@receiver(post_save, sender=Report)
def send_email_to_moderators(sender, instance, **kwargs):

    obj = instance.content_object

    if obj:
        name = obj._meta.verbose_name.title()

        try:
            protocol = settings.PROTOCOL
        except:
            protocol = 'http'

        try:
            admin_url = urlresolvers.reverse("admin:%s_%s_change" %
                                             (obj._meta.app_label,
                                              obj._meta.model_name),
                                             args=(obj.pk,))
        except:
            admin_url = ''

        recievers = []
        for user in get_user_model().objects.filter(is_superuser=True):
            recievers.append(user.email)

        context = Context({
            'site': Site.objects.get_current(),
            'name': name,
            'admin_url': admin_url,
            'protocol': protocol,
            'description': instance.description
        })

        emails.send_email_with_template(recievers, 'report', context)
    else:
        pass


@receiver(post_save, sender=Report)
def send_email_to_creator(sender, instance, **kwargs):
    pass
