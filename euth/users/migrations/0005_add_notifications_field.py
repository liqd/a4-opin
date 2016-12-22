# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_users', '0004_add-user-profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='get_notifications',
            field=models.BooleanField(default=True, help_text='Designates whether you want to receive notifications. Unselect if you do not want to receive notifications.', verbose_name='Send me email notifications')
        )
    ]
