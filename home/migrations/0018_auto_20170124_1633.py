# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20170123_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='color',
            field=models.CharField(max_length=9, choices=[('pink', 'Pink'), ('purple', 'Purple'), ('turquoise', 'Turquoise'), ('blue', 'Blue'), ('orange', 'Orange')], default='blue', blank=True),
        ),
        migrations.AlterField(
            model_name='manualssectionpage',
            name='color',
            field=models.CharField(max_length=9, choices=[('pink', 'Pink'), ('purple', 'Purple'), ('turquoise', 'Turquoise'), ('blue', 'Blue'), ('orange', 'Orange')], default='blue'),
        ),
    ]
