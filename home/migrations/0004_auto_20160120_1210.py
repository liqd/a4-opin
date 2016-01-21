# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailimages.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('home', '0003_simplepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='wagtailcore.Page', parent_link=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePageCarouselItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('embed_url', models.URLField(blank=True, verbose_name='Embed URL')),
                ('image', models.ForeignKey(related_name='+', to='wagtailimages.Image', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Homepage'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_da',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image'))), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('image_text', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_column', wagtail.wagtailcore.blocks.TextBlock())))), ('text_image', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.TextBlock()), ('right_column', wagtail.wagtailimages.blocks.ImageChooserBlock()))))), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('image_text', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_column', wagtail.wagtailcore.blocks.TextBlock())))), ('text_image', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.TextBlock()), ('right_column', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('embed_text', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailembeds.blocks.EmbedBlock()), ('right_column', wagtail.wagtailcore.blocks.TextBlock())))), ('text_embed', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.TextBlock()), ('right_column', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('three_images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock())))), ('collapsible_text', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.TextBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()))))), null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image'))), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_it',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image'))), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_sl',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image'))), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_sv',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image'))), null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_da',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_de',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_en',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_fr',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_it',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_sl',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='title_sv',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('image_text', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_column', wagtail.wagtailcore.blocks.TextBlock())))), ('text_image', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.TextBlock()), ('right_column', wagtail.wagtailimages.blocks.ImageChooserBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('image_text', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_column', wagtail.wagtailcore.blocks.TextBlock())))), ('text_image', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.TextBlock()), ('right_column', wagtail.wagtailimages.blocks.ImageChooserBlock())))), ('embed_text', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailembeds.blocks.EmbedBlock()), ('right_column', wagtail.wagtailcore.blocks.TextBlock())))), ('text_embed', wagtail.wagtailcore.blocks.StructBlock((('left_column', wagtail.wagtailcore.blocks.TextBlock()), ('right_column', wagtail.wagtailembeds.blocks.EmbedBlock())))), ('three_images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock())))), ('collapsible_text', wagtail.wagtailcore.blocks.StructBlock((('heading', wagtail.wagtailcore.blocks.TextBlock()), ('text', wagtail.wagtailcore.blocks.TextBlock()))))), null=True),
        ),
        migrations.AddField(
            model_name='homepagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='carousel_items', to='home.HomePage'),
        ),
    ]
