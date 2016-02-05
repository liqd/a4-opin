# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import modelcluster.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('home', '0006_auto_20160129_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('menu_title', models.CharField(max_length=255)),
                ('menu_title_de', models.CharField(blank=True, max_length=255)),
                ('menu_title_it', models.CharField(blank=True, max_length=255)),
                ('menu_title_fr', models.CharField(blank=True, max_length=255)),
                ('menu_title_sv', models.CharField(blank=True, max_length=255)),
                ('menu_title_sl', models.CharField(blank=True, max_length=255)),
                ('menu_title_da', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavigationMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_da',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_de',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_en',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_fr',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_image',
            field=models.ForeignKey(related_name='+', blank=True, to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_it',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_sl',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_sv',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_da',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('news_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('news', wagtail.wagtailcore.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('news_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('news', wagtail.wagtailcore.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('news_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('news', wagtail.wagtailcore.blocks.CharBlock(classname='full title')))))), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('news_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('news', wagtail.wagtailcore.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_it',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('news_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('news', wagtail.wagtailcore.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sl',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('news_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('news', wagtail.wagtailcore.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sv',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('news_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('news', wagtail.wagtailcore.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_da',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('circles', wagtail.wagtailcore.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('name_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('email_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('message_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('circles', wagtail.wagtailcore.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('name_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('email_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('message_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('circles', wagtail.wagtailcore.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('name_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('email_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('message_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.TextBlock(required=False)))))),), icon='collapse-down'))), null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('circles', wagtail.wagtailcore.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('name_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('email_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('message_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_it',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('circles', wagtail.wagtailcore.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('name_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('email_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('message_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sl',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('circles', wagtail.wagtailcore.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('name_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('email_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('message_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sv',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('circles', wagtail.wagtailcore.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('name_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('email_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('message_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.CreateModel(
            name='NavigationMenuItem',
            fields=[
                ('menuitem_ptr', models.OneToOneField(parent_link=True, to='home.MenuItem', auto_created=True, primary_key=True, serialize=False)),
                ('sort_order', models.IntegerField(editable=False, blank=True, null=True)),
                ('parent', modelcluster.fields.ParentalKey(to='home.NavigationMenu', related_name='menu_items')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('home.menuitem', models.Model),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='link_page',
            field=models.ForeignKey(to='wagtailcore.Page', related_name='+'),
        ),
    ]
