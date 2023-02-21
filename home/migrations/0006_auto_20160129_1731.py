# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160128_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_da',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock()))))), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_it',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sl',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sv',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('text', wagtail.blocks.TextBlock()), ('button', wagtail.blocks.StructBlock((('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(classname='full title')), ('video', wagtail.embeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_da',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()))))), null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_fr',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_it',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sl',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sv',
            field=wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.blocks.StructBlock((('left_image', wagtail.images.blocks.ImageChooserBlock()), ('left_image_text', wagtail.blocks.TextBlock()), ('middle_image', wagtail.images.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.blocks.TextBlock()), ('right_image', wagtail.images.blocks.ImageChooserBlock()), ('right_image_text', wagtail.blocks.TextBlock()))))), null=True, blank=True),
        ),
    ]
