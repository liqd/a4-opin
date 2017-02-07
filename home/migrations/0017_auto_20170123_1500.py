# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_change_streamfields_for_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='color',
            field=models.CharField(choices=[('orange', 'Orange'), ('turquoise', 'Turquoise'), ('pink', 'Pink'), ('blue', 'Blue'), ('purple', 'Purple')], max_length=9, default='blue', blank=True),
        ),
        migrations.AlterField(
            model_name='manualssectionpage',
            name='color',
            field=models.CharField(choices=[('orange', 'Orange'), ('turquoise', 'Turquoise'), ('pink', 'Pink'), ('blue', 'Blue'), ('purple', 'Purple')], max_length=9, default='blue'),
        ),
    ]
