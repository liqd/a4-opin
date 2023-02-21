# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.snippets.blocks
import wagtail.images.blocks
import wagtail.fields
import home.models
import wagtail.blocks
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20170206_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body_el',
            field=wagtail.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], icon='cup', help_text='How should this block be displayed?', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], icon='cup', default='vertical', help_text='How should the text and image be aligned?'))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),))), ('column_block', wagtail.blocks.StructBlock((('title_col1', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image_col1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col1', wagtail.blocks.RichTextBlock(required=False)), ('title_col2', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image_col2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col2', wagtail.blocks.RichTextBlock(required=False)), ('title_col3', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image_col3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col3', wagtail.blocks.RichTextBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_ru',
            field=wagtail.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], icon='cup', help_text='How should this block be displayed?', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], icon='cup', default='vertical', help_text='How should the text and image be aligned?'))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),))), ('column_block', wagtail.blocks.StructBlock((('title_col1', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image_col1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col1', wagtail.blocks.RichTextBlock(required=False)), ('title_col2', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image_col2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col2', wagtail.blocks.RichTextBlock(required=False)), ('title_col3', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image_col3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col3', wagtail.blocks.RichTextBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_uk',
            field=wagtail.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], icon='cup', help_text='How should this block be displayed?', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], icon='cup', default='vertical', help_text='How should the text and image be aligned?'))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),))), ('column_block', wagtail.blocks.StructBlock((('title_col1', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image_col1', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col1', wagtail.blocks.RichTextBlock(required=False)), ('title_col2', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image_col2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col2', wagtail.blocks.RichTextBlock(required=False)), ('title_col3', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image_col3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text_col3', wagtail.blocks.RichTextBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_el',
            field=models.CharField(verbose_name='Header Title', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_ru',
            field=models.CharField(verbose_name='Header Title', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_uk',
            field=models.CharField(verbose_name='Header Title', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='body_el',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='body_ru',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='body_uk',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='title_el',
            field=models.CharField(verbose_name='Title', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='title_ru',
            field=models.CharField(verbose_name='Title', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsdetailpage',
            name='title_uk',
            field=models.CharField(verbose_name='Title', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='body_el',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], icon='cup', help_text='How should this block be displayed?', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], icon='cup', default='vertical', help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('inline_images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False)))))), ('columns', wagtail.blocks.ChoiceBlock(choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup', help_text='', required=False))), icon='image')), ('image_text_block_list', wagtail.blocks.StructBlock((('imageTextBlockList', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.TextBlock()))))),)))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='body_ru',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], icon='cup', help_text='How should this block be displayed?', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], icon='cup', default='vertical', help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('inline_images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False)))))), ('columns', wagtail.blocks.ChoiceBlock(choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup', help_text='', required=False))), icon='image')), ('image_text_block_list', wagtail.blocks.StructBlock((('imageTextBlockList', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.TextBlock()))))),)))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='body_uk',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], icon='cup', help_text='How should this block be displayed?', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], icon='cup', default='vertical', help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('inline_images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False)))))), ('columns', wagtail.blocks.ChoiceBlock(choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup', help_text='', required=False))), icon='image')), ('image_text_block_list', wagtail.blocks.StructBlock((('imageTextBlockList', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.TextBlock()))))),)))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='title_el',
            field=models.CharField(verbose_name='Title', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='title_ru',
            field=models.CharField(verbose_name='Title', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualsindex',
            name='title_uk',
            field=models.CharField(verbose_name='Title', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='description_el',
            field=models.CharField(verbose_name='Description', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='description_ru',
            field=models.CharField(verbose_name='Description', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='description_uk',
            field=models.CharField(verbose_name='Description', blank=True, max_length=260),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='title_el',
            field=models.CharField(verbose_name='Title', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='title_ru',
            field=models.CharField(verbose_name='Title', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='manualssectionpage',
            name='title_uk',
            field=models.CharField(verbose_name='Title', blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_title_el',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_title_ru',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_title_uk',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='pagecollection',
            name='title_el',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='pagecollection',
            name='title_ru',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='pagecollection',
            name='title_uk',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='rssimport',
            name='rss_title_el',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='rssimport',
            name='rss_title_ru',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='rssimport',
            name='rss_title_uk',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='body_el',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], icon='cup', help_text='How should this block be displayed?', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], icon='cup', default='vertical', help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('inline_images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False)))))), ('columns', wagtail.blocks.ChoiceBlock(choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup', help_text='', required=False))), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.blocks.StructBlock((('imageTextBlockList', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.TextBlock()))))),))), ('rss_feed', wagtail.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='body_ru',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], icon='cup', help_text='How should this block be displayed?', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], icon='cup', default='vertical', help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('inline_images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False)))))), ('columns', wagtail.blocks.ChoiceBlock(choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup', help_text='', required=False))), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.blocks.StructBlock((('imageTextBlockList', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.TextBlock()))))),))), ('rss_feed', wagtail.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='body_uk',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.RichTextBlock(required=False)), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(choices=[('', 'None'), ('highlight', 'Highlight (blue)'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation'), ('highlight-purple', 'Highlight (purple)')], icon='cup', help_text='How should this block be displayed?', required=False)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('vertical', 'vertical'), ('horizontal', 'horizontal')], icon='cup', default='vertical', help_text='How should the text and image be aligned?'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('inline_images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False)))))), ('columns', wagtail.blocks.ChoiceBlock(choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup', help_text='', required=False))), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.blocks.StructBlock((('imageTextBlockList', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.blocks.TextBlock()))))),))), ('rss_feed', wagtail.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), verbose_name='body', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_el',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_ru',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='intro_uk',
            field=models.CharField(verbose_name='Subtitle', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='title_el',
            field=models.CharField(verbose_name='Title', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='title_ru',
            field=models.CharField(verbose_name='Title', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='title_uk',
            field=models.CharField(verbose_name='Title', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='color',
            field=models.CharField(choices=[('orange', 'Orange'), ('turquoise', 'Turquoise'), ('purple', 'Purple'), ('blue', 'Blue'), ('pink', 'Pink')], blank=True, default='blue', max_length=9),
        ),
        migrations.AlterField(
            model_name='manualssectionpage',
            name='color',
            field=models.CharField(choices=[('orange', 'Orange'), ('turquoise', 'Turquoise'), ('purple', 'Purple'), ('blue', 'Blue'), ('pink', 'Pink')], default='blue', max_length=9),
        ),
    ]
