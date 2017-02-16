# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_change_streamfields_for_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagecollection',
            name='highlighted_page',
        ),
        migrations.AddField(
            model_name='pagecollection',
            name='intro_text',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='color',
            field=models.CharField(blank=True, max_length=9, default='blue', choices=[('blue', 'Blue'), ('purple', 'Purple'), ('pink', 'Pink'), ('orange', 'Orange'), ('turquoise', 'Turquoise')]),
        ),
        migrations.AlterField(
            model_name='manualssectionpage',
            name='color',
            field=models.CharField(max_length=9, default='blue', choices=[('blue', 'Blue'), ('purple', 'Purple'), ('pink', 'Pink'), ('orange', 'Orange'), ('turquoise', 'Turquoise')]),
        ),
    ]
