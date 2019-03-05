# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(help_text='Required. 60 characters or fewer. Letters, digits, spaces and @/./+/-/_ only.', unique=True, verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, max_length=60, validators=[django.core.validators.RegexValidator('^[\\w]+[ \\w.@+-]*$', 'Enter a valid username. This value may contain only letters, digits, spaces and @/./+/-/_ characters. It must start with a digit or a letter.', 'invalid')])),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email address', error_messages={'unique': 'A user with that email address already exists.'})),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(editable=False, default=django.utils.timezone.now)),
                ('avatar', models.ImageField(blank=True, upload_to='users/images')),
                ('groups', models.ManyToManyField(blank=True, verbose_name='groups', to='auth.Group', related_name='user_set', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(blank=True, verbose_name='user permissions', to='auth.Permission', related_name='user_set', related_query_name='user', help_text='Specific permissions for this user.')),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('token', models.UUIDField(unique=True, default=uuid.uuid4)),
                ('username', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField(max_length=128)),
                ('next_action', models.URLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reset',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('token', models.UUIDField(unique=True, default=uuid.uuid4)),
                ('next_action', models.URLField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
        ),
    ]
