# Generated by Django 3.2.20 on 2024-09-10 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_offlinephases', '0006_alter_offlineevent_file_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offlineeventfileupload',
            name='offlineevent',
        ),
        migrations.DeleteModel(
            name='OfflineEvent',
        ),
        migrations.DeleteModel(
            name='OfflineEventFileUpload',
        ),
    ]