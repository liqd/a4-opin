# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.images.blocks
import wagtail.core.fields
import wagtail.snippets.blocks
import wagtail.embeds.blocks
import home.models
import wagtail.core.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20160208_1401'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSSImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('url', models.URLField(null=True, blank=True)),
                ('rss_title', models.CharField(max_length=255)),
                ('rss_title_de', models.CharField(blank=True, max_length=255)),
                ('rss_title_it', models.CharField(blank=True, max_length=255)),
                ('rss_title_fr', models.CharField(blank=True, max_length=255)),
                ('rss_title_sv', models.CharField(blank=True, max_length=255)),
                ('rss_title_sl', models.CharField(blank=True, max_length=255)),
                ('rss_title_da', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_da',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('news', wagtail.core.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('news', wagtail.core.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('news', wagtail.core.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('news', wagtail.core.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_it',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('news', wagtail.core.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sl',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('news', wagtail.core.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sv',
            field=wagtail.core.fields.StreamField((('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('video_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('news', wagtail.core.blocks.CharBlock(classname='full title'))))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_da',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(required=False, help_text='', choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup'))), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, verbose_name='body', blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(required=False, help_text='', choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup'))), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, verbose_name='body', blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(required=False, help_text='', choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup'))), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, verbose_name='body', blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_fr',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(required=False, help_text='', choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup'))), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, verbose_name='body', blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_it',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(required=False, help_text='', choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup'))), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, verbose_name='body', blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sl',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(required=False, help_text='', choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup'))), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, verbose_name='body', blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sv',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('info_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(required=False, classname='full title')), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False)), ('button', wagtail.core.blocks.StructBlock((('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.core.blocks.ChoiceBlock(required=False, help_text='How should this block be displayed?', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed'), ('boxed2', 'Boxed Variation')], icon='cup'))))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.core.blocks.StructBlock((('inline_images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(required=False)))))), ('columns', wagtail.core.blocks.ChoiceBlock(required=False, help_text='', choices=[('4', 'three columns'), ('6', 'two columns')], icon='cup'))), icon='image')), ('contact_block', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(classname='full title')), ('name_label', wagtail.core.blocks.CharBlock(classname='full title')), ('email_label', wagtail.core.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.core.blocks.CharBlock(classname='full title')), ('message_label', wagtail.core.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.core.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.core.blocks.StructBlock((('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False)))))),), icon='collapse-down')), ('image_text_block_list', wagtail.core.blocks.StructBlock((('imageTextBlockList', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.TextBlock()))))),))), ('rss_feed', wagtail.core.blocks.StructBlock((('feed', wagtail.snippets.blocks.SnippetChooserBlock(target_model=home.models.snippets.RSSImport, required=True)),)))), null=True, verbose_name='body', blank=True),
        ),
    ]
