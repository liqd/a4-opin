# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_users', '0005_add_notifications_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_avatar',
            field=models.ImageField(upload_to='users/images', blank=True, verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='get_notifications',
            field=models.BooleanField(verbose_name='Send me email notifications', default=True, help_text='Designates whether you want to receivenotifications. Unselect if you do not want to receive notifications.'),
        ),
    ]
