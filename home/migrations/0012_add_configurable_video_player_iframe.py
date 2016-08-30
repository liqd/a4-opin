# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20160830_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='videoplayer_url',
            field=models.URLField(default='https://player.vimeo.com/video/43476107'),
            preserve_default=False,
        ),
    ]
