# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.images.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('home', '0008_create_menus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(verbose_name='Header Image', related_name='+', to='wagtailimages.Image', help_text='The Image that is shown on top of the page', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_da',
            field=models.CharField(verbose_name='Header Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_de',
            field=models.CharField(verbose_name='Header Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(verbose_name='Header Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_fr',
            field=models.CharField(verbose_name='Header Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_it',
            field=models.CharField(verbose_name='Header Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_sl',
            field=models.CharField(verbose_name='Header Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='title_sv',
            field=models.CharField(verbose_name='Header Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_da',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.core.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.core.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.core.blocks.TextBlock()), ('circles', wagtail.core.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.TextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.core.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.core.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.core.blocks.TextBlock()), ('circles', wagtail.core.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.TextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.core.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.core.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.core.blocks.TextBlock()), ('circles', wagtail.core.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.TextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_fr',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.core.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.core.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.core.blocks.TextBlock()), ('circles', wagtail.core.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.TextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_it',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.core.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.core.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.core.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.core.blocks.TextBlock()), ('circles', wagtail.core.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.TextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sl',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.core.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.core.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.core.blocks.TextBlock()), ('circles', wagtail.core.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.TextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sv',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.core.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.core.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.core.blocks.TextBlock()), ('circles', wagtail.core.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.TextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='intro_da',
            field=models.CharField(verbose_name='Subtitle', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='intro_de',
            field=models.CharField(verbose_name='Subtitle', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='intro_en',
            field=models.CharField(verbose_name='Subtitle', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='intro_fr',
            field=models.CharField(verbose_name='Subtitle', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='intro_it',
            field=models.CharField(verbose_name='Subtitle', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='intro_sl',
            field=models.CharField(verbose_name='Subtitle', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='intro_sv',
            field=models.CharField(verbose_name='Subtitle', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='title_da',
            field=models.CharField(verbose_name='Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='title_de',
            field=models.CharField(verbose_name='Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='title_en',
            field=models.CharField(verbose_name='Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='title_fr',
            field=models.CharField(verbose_name='Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='title_it',
            field=models.CharField(verbose_name='Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='title_sl',
            field=models.CharField(verbose_name='Title', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='title_sv',
            field=models.CharField(verbose_name='Title', max_length=255, blank=True),
        ),
        migrations.DeleteModel(
            name='AboutPage',
        ),
    ]
