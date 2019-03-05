# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import home.models
import wagtail.core.blocks
import wagtail.snippets.blocks
import wagtail.images.blocks
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_homepage_add_editable_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_ka',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?')), ('alignment', wagtail.core.blocks.ChoiceBlock(icon='cup', choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?'))))), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('news', wagtail.core.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(required=True, target_model=home.models.snippets.RSSImport)),))), ('column_block', wagtail.core.blocks.StructBlock((('title_col1', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('image_col1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col1', wagtail.core.blocks.RichTextBlock(required=False)), ('title_col2', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('image_col2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col2', wagtail.core.blocks.RichTextBlock(required=False)), ('title_col3', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('image_col3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col3', wagtail.core.blocks.RichTextBlock(required=False)))))), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_ka',
            field=models.CharField(default='Ever wondered how to get young people involved in politics online?OPIN, a European toolbox for youth eParticipation projects, shows you how.', max_length=255, verbose_name='Subtitle', blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_ka',
            field=models.CharField(max_length=255, verbose_name='Header Title', blank=True),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='body_ka',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, verbose_name='body', blank=True),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='title_ka',
            field=models.CharField(max_length=150, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='body_ka',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?')), ('alignment', wagtail.core.blocks.ChoiceBlock(icon='cup', choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('4', 'three columns'), ('6', 'two columns')], help_text=''))), icon='image')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),)))), null=True, verbose_name='body', blank=True),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='title_ka',
            field=models.CharField(max_length=150, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='description_ka',
            field=models.CharField(max_length=260, verbose_name='Description', blank=True),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='title_ka',
            field=models.CharField(max_length=150, verbose_name='Title', blank=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_title_ka',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='pagecollection',
            name='title_ka',
            field=models.CharField(max_length=80, blank=True),
        ),
        migrations.AddField(
            model_name='rssimport',
            name='rss_title_ka',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='body_ka',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?')), ('alignment', wagtail.core.blocks.ChoiceBlock(icon='cup', choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(icon='cup', required=False, choices=[('4', 'three columns'), ('6', 'two columns')], help_text=''))), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(required=True, target_model=home.models.snippets.RSSImport)),)))), null=True, verbose_name='body', blank=True),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_ka',
            field=models.CharField(max_length=255, verbose_name='Subtitle', blank=True),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='title_ka',
            field=models.CharField(max_length=255, verbose_name='Title', blank=True),
        ),
    ]
