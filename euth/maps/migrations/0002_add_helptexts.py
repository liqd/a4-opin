# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import euth.maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_maps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapidea',
            name='point',
            field=euth.maps.fields.PointField(verbose_name='Where can your idea be located on a map?', help_text='Click inside marked area to set a marker. Drag and drop marker to change place.'),
        ),
    ]
