# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import home.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailsnippets.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_mt',
            field=wagtail.wagtailcore.fields.StreamField((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?')), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?'))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('news_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('news', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.wagtailcore.blocks.StructBlock((('feed', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(required=True, target_model=home.models.RSSImport)),))), ('column_block', wagtail.wagtailcore.blocks.StructBlock((('title_col1', wagtail.wagtailcore.blocks.CharBlock(required=False, classname='full title')), ('image_col1', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text_col1', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('title_col2', wagtail.wagtailcore.blocks.CharBlock(required=False, classname='full title')), ('image_col2', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text_col2', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('title_col3', wagtail.wagtailcore.blocks.CharBlock(required=False, classname='full title')), ('image_col3', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text_col3', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))), blank=True, null=True),
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
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), blank=True, verbose_name='body', null=True),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='title_mt',
            field=models.CharField(blank=True, max_length=150, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='body_mt',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?')), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?'))))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('inline_images', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False)))))), ('columns', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', required=False, choices=[('4', 'three columns'), ('6', 'two columns')], help_text=''))), icon='image')), ('image_text_block_list', wagtail.wagtailcore.blocks.StructBlock((('imageTextBlockList', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()))))),)))), blank=True, verbose_name='body', null=True),
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
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', required=False, choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], help_text='How should this block be displayed?')), ('alignment', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], help_text='How should the text and image be aligned?'))))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('inline_images', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False)))))), ('columns', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', required=False, choices=[('4', 'three columns'), ('6', 'two columns')], help_text=''))), icon='image')), ('contact_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('name_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('email_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('message_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.wagtailcore.blocks.StructBlock((('imageTextBlockList', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()))))),))), ('rss_feed', wagtail.wagtailcore.blocks.StructBlock((('feed', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(required=True, target_model=home.models.RSSImport)),)))), blank=True, verbose_name='body', null=True),
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
