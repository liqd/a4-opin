# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import django.db.models.deletion
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('home', '0003_simplepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, to='wagtailcore.Page', serialize=False, on_delete=models.CASCADE)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Homepage'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_da',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.core.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(required=False)), ('text', wagtail.core.blocks.TextBlock()), ('internal_link', wagtail.core.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.core.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(required=False)), ('text', wagtail.core.blocks.TextBlock()), ('internal_link', wagtail.core.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.core.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(required=False)), ('text', wagtail.core.blocks.TextBlock()), ('internal_link', wagtail.core.blocks.URLBlock(required=False)))))), null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.core.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(required=False)), ('text', wagtail.core.blocks.TextBlock()), ('internal_link', wagtail.core.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_it',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.core.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(required=False)), ('text', wagtail.core.blocks.TextBlock()), ('internal_link', wagtail.core.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_sl',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.core.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(required=False)), ('text', wagtail.core.blocks.TextBlock()), ('internal_link', wagtail.core.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_sv',
            field=wagtail.core.fields.StreamField((('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.core.blocks.StructBlock((('background_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='none')), ('font_colour', wagtail.core.blocks.ChoiceBlock(choices=[('none', 'none'), ('inverse', 'inverse'), ('danger', 'danger')], default='black')), ('heading', wagtail.core.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(required=False)), ('text', wagtail.core.blocks.TextBlock()), ('internal_link', wagtail.core.blocks.URLBlock(required=False)))))), blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image', blank=True, related_name='+'),
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
            field=models.CharField(max_length=255, default=0),
            preserve_default=False,
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
    ]
