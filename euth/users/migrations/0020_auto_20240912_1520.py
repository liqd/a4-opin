# Generated by Django 3.2.20 on 2024-09-12 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_users', '0019_alter_user_timezone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='_avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='facebook_handle',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='get_notifications',
        ),
        migrations.RemoveField(
            model_name='user',
            name='instagram_handle',
        ),
        migrations.RemoveField(
            model_name='user',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='user',
            name='timezone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='twitter_handle',
        ),
    ]