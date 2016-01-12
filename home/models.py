from __future__ import unicode_literals

from django.db import models
from contrib.translations.translations import TranslatedField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel


class HomePage(Page):
	pass



class SimplePage(Page):

	# Title
	title_en = models.CharField(max_length=255)
	title_de = models.CharField(max_length=255)
	title_it = models.CharField(max_length=255)
	title_fr = models.CharField(max_length=255)
	title_sv = models.CharField(max_length=255)
	title_sl = models.CharField(max_length=255)

    # Body
	body_en = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True)

	body_de = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True)

	body_it = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True)

	body_fr = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True)

	body_sv = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True)

	body_sl = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True)

	translated_title = TranslatedField(
        'title_de',
        'title_it',
        'title_en',
        'title_fr',
        'title_sv',
        'title_sl',
    )

	body = TranslatedField(
        'body_de',
        'body_it',
        'body_en',
        'body_fr',
        'body_sv',
        'body_sl',
    )

SimplePage.content_panels = [

	FieldPanel('title'),
	MultiFieldPanel (
		[
			FieldPanel('title_en'),
			StreamFieldPanel('body_en')
		],
	 	heading = "English",
	 	classname = "collapsible collapsed"
	),
	MultiFieldPanel (
		[
			FieldPanel('title_de'),
			StreamFieldPanel('body_de')
		],
	 	heading = "German",
	 	classname = "collapsible collapsed"
	),
	MultiFieldPanel (
		[
			FieldPanel('title_it'),
			StreamFieldPanel('body_it')
		],
	 	heading = "Italien",
	 	classname = "collapsible collapsed"
	),
	MultiFieldPanel (
		[
			FieldPanel('title_fr'),
			StreamFieldPanel('body_fr')
		],
	 	heading = "French",
	 	classname = "collapsible collapsed"
	),
	MultiFieldPanel (
		[
			FieldPanel('title_sv'),
			StreamFieldPanel('body_sv')
		],
	 	heading = "Swedish",
	 	classname = "collapsible collapsed"
	),
	MultiFieldPanel (
		[
			FieldPanel('title_sl'),
			StreamFieldPanel('body_sl')
		],
	 	heading = "Slovakian",
	 	classname = "collapsible collapsed"
	)

]
