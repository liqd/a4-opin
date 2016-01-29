# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160128_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_da',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()))))), null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_it',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sl',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_sv',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('info_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title', required=False)), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('text', wagtail.wagtailcore.blocks.TextBlock()), ('button', wagtail.wagtailcore.blocks.StructBlock((('internal_link', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_text', wagtail.wagtailcore.blocks.TextBlock(required=False))), required=False)), ('highlight', wagtail.wagtailcore.blocks.ChoiceBlock(icon='cup', choices=[('', 'None'), ('highlight', 'Highlight'), ('boxed', 'Boxed')], help_text='How should this block be displayed?', required=False))))), ('video_block', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('video', wagtail.wagtailembeds.blocks.EmbedBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_da',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()))))), null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_it',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sl',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()))))), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_sv',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(icon='title', classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.TextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('images', wagtail.wagtailcore.blocks.StructBlock((('left_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('left_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('middle_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('middle_image_text', wagtail.wagtailcore.blocks.TextBlock()), ('right_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('right_image_text', wagtail.wagtailcore.blocks.TextBlock()))))), null=True, blank=True),
        ),
    ]
