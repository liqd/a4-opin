# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.fields
import wagtail.images.blocks
import modelcluster.fields
import wagtail.blocks
import wagtail.embeds.blocks
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
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title')))))), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_it',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sl',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sv',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', help_text='How should this block be displayed?', required=False, choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')]))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock())))), ('news_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('news', wagtail.blocks.CharBlock(classname='full title')))))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_da',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()), ('circles', wagtail.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()), ('circles', wagtail.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()), ('circles', wagtail.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form')), ('accordion_block', wagtail.blocks.StructBlock((('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.TextBlock(required=False)), ('content', wagtail.blocks.TextBlock(required=False)))))),), icon='collapse-down'))), null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_fr',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()), ('circles', wagtail.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_it',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()), ('circles', wagtail.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sl',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()), ('circles', wagtail.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sv',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('rich_text', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('wide_image', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()),), icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()), ('circles', wagtail.blocks.BooleanBlock())), icon='image')), ('contact_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('name_label', wagtail.blocks.CharBlock(classname='full title')), ('email_label', wagtail.blocks.CharBlock(classname='full title')), ('subject_label', wagtail.blocks.CharBlock(classname='full title')), ('message_label', wagtail.blocks.CharBlock(classname='full title')), ('submit_label', wagtail.blocks.CharBlock(classname='full title'))), icon='form'))), blank=True, null=True),
        ),
        migrations.CreateModel(
            name='NavigationMenuItem',
            fields=[
                ('menuitem_ptr', models.OneToOneField(parent_link=True, to='home.MenuItem', auto_created=True, primary_key=True, serialize=False, on_delete=models.CASCADE)),
                ('sort_order', models.IntegerField(editable=False, blank=True, null=True)),
                ('parent', modelcluster.fields.ParentalKey(to='home.NavigationMenu', related_name='menu_items', on_delete=models.CASCADE)),
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
            field=models.ForeignKey(to='wagtailcore.Page', related_name='+', on_delete=models.CASCADE),
        ),
    ]
