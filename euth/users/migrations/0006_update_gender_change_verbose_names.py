# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import euth.contrib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('euth_users', '0005_add_notifications_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_avatar',
            field=models.ImageField(validators=[euth.contrib.validators.validate_avatar], verbose_name='Avatar picture', blank=True, upload_to='users/images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(verbose_name='Date of birth', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(verbose_name='City of residence', blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(verbose_name='Gender', max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('TF', 'Transgender Female'), ('TM', 'Transgender Male'), ('I', 'Intersex'), ('GF', 'Gender Fluid'), ('O', 'Other')], blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='get_notifications',
            field=models.BooleanField(verbose_name='Send me email notifications', default=True, help_text='Designates whether you want to receivenotifications. Unselect if you do not want to receive notifications.'),
        ),
    ]
