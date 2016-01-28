from django.db import models
from wagtail.wagtailcore.models import Page
from contrib.translations.translations import TranslatedField
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface
from wagtail.wagtailadmin.edit_handlers import ObjectList


@register_snippet
class Organisation(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('url'),
        FieldPanel('name'),
        FieldPanel('link'),
        ImageChooserPanel('logo')
    ]

    def __unicode__(self):
        return self.source + ', ' + self.name


class ProjectPage(Page):

	# Image
	image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

	COMMENTING_TEXT = 'CT'
	IDEA_COLLECTION = 'IC'
	MOBILE_POLLING = 'MP'

	PROJECTTYPE_CHOICES = (
		(COMMENTING_TEXT, 'Commenting Text'),
		(IDEA_COLLECTION, 'Idea Collection'),
		(MOBILE_POLLING, 'Mobile Polling'),
	)

	# Type
	projecttype = models.CharField(max_length=255, choices=PROJECTTYPE_CHOICES)

	# Title
	title_en = models.CharField(max_length=255)
	title_de = models.CharField(max_length=255, blank=True)
	title_it = models.CharField(max_length=255, blank=True)
	title_fr = models.CharField(max_length=255, blank=True)
	title_sv = models.CharField(max_length=255, blank=True)
	title_sl = models.CharField(max_length=255, blank=True)
	title_da = models.CharField(max_length=255, blank=True)

	# teaser
	teaser_en = models.CharField(max_length=255)
	teaser_de = models.CharField(max_length=255, blank=True)
	teaser_it = models.CharField(max_length=255, blank=True)
	teaser_fr = models.CharField(max_length=255, blank=True)
	teaser_sv = models.CharField(max_length=255, blank=True)
	teaser_sl = models.CharField(max_length=255, blank=True)
	teaser_da = models.CharField(max_length=255, blank=True)

	teaser = TranslatedField(
		'body_de',
		'body_it',
		'body_en',
		'body_fr',
		'body_sv',
		'body_sl',
		'body_da',
	)

	translated_title = TranslatedField(
		'title_de',
		'title_it',
		'title_en',
		'title_fr',
		'title_sv',
		'title_sl',
		'title_da',
	)

	content_panels = [

		FieldPanel('title'),
		ImageChooserPanel('image'),
		FieldPanel('type'),

		MultiFieldPanel(
		[
			FieldPanel('title_en'),
			FieldPanel('teaser_en')
		],
		heading="English",
		classname="collapsible collapsed"
		),
		MultiFieldPanel(
		[
			FieldPanel('title_de'),
			FieldPanel('teaser_en')
		],
		heading="German",
		classname="collapsible collapsed"
		),
		MultiFieldPanel(
		[
			FieldPanel('title_it'),
			FieldPanel('teaser_it')
		],
		heading="Italien",
		classname="collapsible collapsed"
		),
		MultiFieldPanel(
		[
			FieldPanel('title_fr'),
			FieldPanel('teaser_fr')
		],
		heading="French",
		classname="collapsible collapsed"
		),
		MultiFieldPanel(
		[
			FieldPanel('title_sv'),
			FieldPanel('teaser_sv')
		],
		heading="Swedish",
		classname="collapsible collapsed"
		),
		MultiFieldPanel(
		[
			FieldPanel('title_sl'),
			FieldPanel('teaser_sl')
		],
		heading="Slovene",
		classname="collapsible collapsed"
		),
		MultiFieldPanel(
		[
			FieldPanel('title_da'),
			FieldPanel('teaser_da')
		],
		heading="Danish",
		classname="collapsible collapsed"
		)

	]
	edit_handler = TabbedInterface([
	ObjectList(content_panels, heading='Content'),
	ObjectList(Page.promote_panels, heading='Promote'),
	ObjectList(
	Page.settings_panels, heading='Settings', classname="settings"),
	])



