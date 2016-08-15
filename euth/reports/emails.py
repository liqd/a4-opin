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


