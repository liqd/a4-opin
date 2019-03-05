# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('euth_actions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='actor',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
        ),
    ]
