# Generated by Django 2.2.12 on 2020-04-28 16:11

import adhocracy4.images.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_communitydebate', '0002_topic_add_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=adhocracy4.images.fields.ConfiguredImageField('idea_image', blank=True, upload_to='communitydebate/images'),
        ),
    ]
