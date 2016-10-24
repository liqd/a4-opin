# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import euth.contrib.validators
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('euth_projects', '0004_use-autoslug-filed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(help_text='This short description will appear on the header of the project and in the teaser. It should briefly state the goal of the project in max. 120 chars.', verbose_name='Short description of your project', max_length=120),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/backgrounds', verbose_name='Header image', help_text='The image will be shown as a decorative background image. It must be min. 1300px wide and 600px tall. Allowed file formats are .jpg and .png. The file size should be max. 2 MB.', validators=[euth.contrib.validators.validate_hero_image], blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='information',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='This description should tell participants what the goal of the project is, how the project’s participation will look like. It will be always visible in the „Info“ tab on your project’s page.', verbose_name='Description of your project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text='This title will appear on the teaser card and on top of the project detail page. It should be max. 120 characters long', verbose_name='Title of your project', max_length=120),
        ),
    ]
