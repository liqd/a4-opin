# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_add_ukrainian_greek_russian_translations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='color',
            field=models.CharField(default='blue', blank=True, choices=[('blue', 'Blue'), ('orange', 'Orange'), ('turquoise', 'Turquoise'), ('pink', 'Pink'), ('purple', 'Purple')], max_length=9),
        ),
        migrations.AlterField(
            model_name='manualssectionpage',
            name='color',
            field=models.CharField(default='blue', choices=[('blue', 'Blue'), ('orange', 'Orange'), ('turquoise', 'Turquoise'), ('pink', 'Pink'), ('purple', 'Purple')], max_length=9),
        ),
    ]
