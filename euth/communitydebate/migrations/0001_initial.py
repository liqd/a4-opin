# Generated by Django 2.2.12 on 2020-04-17 15:30

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a4modules', '0005_module_is_draft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='a4modules.Item')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('name', models.CharField(max_length=120)),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('a4modules.item',),
        ),
    ]