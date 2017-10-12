# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import adhocracy4.maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_maps', '0004_move_area_settings_to_a4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areasettings',
            name='module',
        ),
        migrations.AlterField(
            model_name='mapidea',
            name='point',
            field=adhocracy4.maps.fields.PointField(verbose_name='Where can your idea be located on a map?', help_text='Click inside marked area to set a marker. Drag and drop marker to change place.'),
        ),
        migrations.DeleteModel(
            name='AreaSettings',
        ),
    ]
