# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.fields
import wagtail.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_add_manual_index_and_section_page_and_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_da',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_de',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_en',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_fr',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_it',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_sl',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_sv',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='color',
            field=models.CharField(max_length=9, blank=True, choices=[('turquoise', 'Turquoise'), ('purple', 'Purple'), ('pink', 'Pink'), ('orange', 'Orange'), ('blue', 'Blue')], default='blue'),
        ),
        migrations.AlterField(
            model_name='manualssectionpage',
            name='color',
            field=models.CharField(max_length=9, choices=[('turquoise', 'Turquoise'), ('purple', 'Purple'), ('pink', 'Pink'), ('orange', 'Orange'), ('blue', 'Blue')], default='blue'),
        ),
    ]
