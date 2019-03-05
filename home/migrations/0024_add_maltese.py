# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import home.models
import wagtail.core.blocks
import wagtail.snippets.blocks
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_mt',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?')), ('alignment', wagtail.core.blocks.ChoiceBlock(icon='cup', choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?'))))), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('news', wagtail.core.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(required=True, target_model=home.models.snippets.RSSImport)),))), ('column_block', wagtail.core.blocks.StructBlock((('title_col1', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image_col1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col1', wagtail.core.blocks.RichTextBlock(required=False)), ('title_col2', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image_col2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col2', wagtail.core.blocks.RichTextBlock(required=False)), ('title_col3', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image_col3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col3', wagtail.core.blocks.RichTextBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_mt',
            field=models.CharField(default='Ever wondered how to get young people involved in politics online?OPIN, a European toolbox for youth eParticipation projects, shows you how.', blank=True, max_length=255, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_mt',
            field=models.CharField(blank=True, max_length=255, verbose_name='Header Title'),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='body_mt',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), blank=True, verbose_name='body', null=True),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='title_mt',
            field=models.CharField(blank=True, max_length=150, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='body_mt',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?')), ('alignment', wagtail.core.blocks.ChoiceBlock(icon='cup', choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('4', 'three columns'), ('6', 'two columns')], help_text=''))), icon='image')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),)))), blank=True, verbose_name='body', null=True),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='title_mt',
            field=models.CharField(blank=True, max_length=150, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='description_mt',
            field=models.CharField(blank=True, max_length=260, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='title_mt',
            field=models.CharField(blank=True, max_length=150, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_title_mt',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='pagecollection',
            name='title_mt',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='rssimport',
            name='rss_title_mt',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='body_mt',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?')), ('alignment', wagtail.core.blocks.ChoiceBlock(icon='cup', choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('4', 'three columns'), ('6', 'two columns')], help_text=''))), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(required=True, target_model=home.models.snippets.RSSImport)),)))), blank=True, verbose_name='body', null=True),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_mt',
            field=models.CharField(blank=True, max_length=255, verbose_name='Subtitle'),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='title_mt',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
    ]
