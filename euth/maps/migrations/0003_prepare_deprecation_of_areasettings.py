# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('euth_maps', '0002_add_helptexts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areasettings',
            name='module',
            field=models.OneToOneField(related_name='areasettings_settings_legacy', to='a4modules.Module', on_delete=models.CASCADE),
        ),
    ]
