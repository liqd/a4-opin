# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_users', '0006_change_avatar_validator_and_helptext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_avatar',
            field=models.ImageField(verbose_name='Avatar picture', upload_to='users/images', blank=True),
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
            field=models.CharField(verbose_name='Gender', max_length=1, blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('TF', 'Transgender Female'), ('TM', 'Transgender Male'), ('I', 'Intersex'), ('GF', 'Gender Fluid'), ('O', 'Other')]),
        ),
    ]
