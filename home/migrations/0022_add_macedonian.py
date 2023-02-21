# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.snippets.blocks
import wagtail.images.blocks
import wagtail.fields
import wagtail.blocks
import wagtail.embeds.blocks
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_add_georgian'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_mk',
            field=wagtail.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?', icon='cup')), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?', icon='cup'))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),))), ('column_block', wagtail.blocks.StructBlock((('title_col1', wagtail.blocks.CharBlock(required=False, classname='full title')), ('image_col1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col1', wagtail.blocks.RichTextBlock(required=False)), ('title_col2', wagtail.blocks.CharBlock(required=False, classname='full title')), ('image_col2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col2', wagtail.blocks.RichTextBlock(required=False)), ('title_col3', wagtail.blocks.CharBlock(required=False, classname='full title')), ('image_col3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col3', wagtail.blocks.RichTextBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_mk',
            field=models.CharField(blank=True, verbose_name='Subtitle', default='Ever wondered how to get young people involved in politics online?OPIN, a European toolbox for youth eParticipation projects, shows you how.', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_mk',
            field=models.CharField(blank=True, verbose_name='Header Title', max_length=255),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='body_mk',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), blank=True, verbose_name='body', null=True),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='title_mk',
            field=models.CharField(blank=True, verbose_name='Title', max_length=150),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='body_mk',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?', icon='cup')), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?', icon='cup'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('inline_images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False)))))), ('columns', wagtail.blocks.ChoiceBlock(required=False, choices=[('4', 'three columns'), ('6', 'two columns')], help_text='', icon='cup'))), icon='image')), ('image_text_block_list', wagtail.blocks.StructBlock((('imageTextBlockList', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.TextBlock()))))),)))), blank=True, verbose_name='body', null=True),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='title_mk',
            field=models.CharField(blank=True, verbose_name='Title', max_length=150),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='description_mk',
            field=models.CharField(blank=True, verbose_name='Description', max_length=260),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='title_mk',
            field=models.CharField(blank=True, verbose_name='Title', max_length=150),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_title_mk',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='pagecollection',
            name='title_mk',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='rssimport',
            name='rss_title_mk',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='body_mk',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?', icon='cup')), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?', icon='cup'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('inline_images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False)))))), ('columns', wagtail.blocks.ChoiceBlock(required=False, choices=[('4', 'three columns'), ('6', 'two columns')], help_text='', icon='cup'))), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.blocks.StructBlock((('imageTextBlockList', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.TextBlock()))))),))), ('rss_feed', wagtail.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), blank=True, verbose_name='body', null=True),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_mk',
            field=models.CharField(blank=True, verbose_name='Subtitle', max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='title_mk',
            field=models.CharField(blank=True, verbose_name='Title', max_length=255),
        ),
    ]
