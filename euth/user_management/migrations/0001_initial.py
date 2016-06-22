# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django.contrib.auth.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(help_text='Required. 60 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.', error_messages={'unique': 'A user with that username already exists.'}, unique=True, max_length=60, verbose_name='username', validators=[django.core.validators.RegexValidator('^[ \\w.@+-]+$', 'Enter a valid username. This value may contain only letters, digits, spacesand @/./+/-/_ characters.', 'invalid')])),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email address already exists.'}, verbose_name='email address', max_length=254, unique=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', related_query_name='user', verbose_name='groups', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', to='auth.Permission', related_query_name='user', verbose_name='user permissions', related_name='user_set')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('token', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('username', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField(max_length=128)),
                ('next_action', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
