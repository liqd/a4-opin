# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import euth.contrib.validators


class Migration(migrations.Migration):

    dependencies = [
        ('euth_users', '0002_auto_20160715_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users/images', validators=[euth.contrib.validators.validate_logo]),
        ),
    ]
