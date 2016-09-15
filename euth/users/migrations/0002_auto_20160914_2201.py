# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.RemoveField(
            model_name='reset',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Users', 'verbose_name': 'User'},
        ),
        migrations.DeleteModel(
            name='Reset',
        ),
    ]
