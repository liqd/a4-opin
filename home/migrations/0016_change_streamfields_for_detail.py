# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_add_manual_index_and_section_page_and_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_da',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_it',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_sl',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
        ),
        migrations.AlterField(
            model_name='manualsdetailpage',
            name='body_sv',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('accordion_block', wagtail.wagtailcore.blocks.StructBlock((('accordion_items', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('content', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))))),), icon='collapse-down'))), null=True, blank=True, verbose_name='body'),
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
