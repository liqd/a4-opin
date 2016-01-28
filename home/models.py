from __future__ import unicode_literals

from django.db import models
from contrib.translations.translations import TranslatedField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface
from wagtail.wagtailadmin.edit_handlers import ObjectList

from modelcluster.fields import ParentalKey

from .blocks import InfoBlock

# Pages

class HomePage(Page):

    # Title
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255, blank=True)
    title_it = models.CharField(max_length=255, blank=True)
    title_fr = models.CharField(max_length=255, blank=True)
    title_sv = models.CharField(max_length=255, blank=True)
    title_sl = models.CharField(max_length=255, blank=True)
    title_da = models.CharField(max_length=255, blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Body
    body_en = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
    ], null=True)

    body_de = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
    ], null=True, blank=True)

    body_it = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
    ], null=True, blank=True)

    body_fr = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
    ], null=True, blank=True)

    body_sv = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
    ], null=True, blank=True)

    body_sl = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
    ], null=True, blank=True)

    body_da = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
    ], null=True, blank=True)

    body = TranslatedField(
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

    class Meta:
        verbose_name = "Homepage"

    content_panels = [

        FieldPanel('title'),
        ImageChooserPanel('image'),

        MultiFieldPanel(
            [
                FieldPanel('title_en'),
                StreamFieldPanel('body_en')
            ],
            heading="English",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_de'),
                StreamFieldPanel('body_de')
            ],
            heading="German",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_it'),
                StreamFieldPanel('body_it')
            ],
            heading="Italien",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_fr'),
                StreamFieldPanel('body_fr')
            ],
            heading="French",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sv'),
                StreamFieldPanel('body_sv')
            ],
            heading="Swedish",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sl'),
                StreamFieldPanel('body_sl')
            ],
            heading="Slovene",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_da'),
                StreamFieldPanel('body_da')
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

    parent_page_types = []


class SimplePage(Page):

    # Title
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255, blank=True)
    title_it = models.CharField(max_length=255, blank=True)
    title_fr = models.CharField(max_length=255, blank=True)
    title_sv = models.CharField(max_length=255, blank=True)
    title_sl = models.CharField(max_length=255, blank=True)
    title_da = models.CharField(max_length=255, blank=True)

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
    ], null=True, blank=True)

    body_it = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True, blank=True)

    body_fr = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True, blank=True)

    body_sv = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True, blank=True)

    body_sl = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True, blank=True)

    body_da = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
    ], null=True, blank=True)

    translated_title = TranslatedField(
        'title_de',
        'title_it',
        'title_en',
        'title_fr',
        'title_sv',
        'title_sl',
        'title_da',
    )

    body = TranslatedField(
        'body_de',
        'body_it',
        'body_en',
        'body_fr',
        'body_sv',
        'body_sl',
        'body_da',
    )

    content_panels = [

        FieldPanel('title'),
        MultiFieldPanel(
            [
                FieldPanel('title_en'),
                StreamFieldPanel('body_en')
            ],
            heading="English",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_de'),
                StreamFieldPanel('body_de')
            ],
            heading="German",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_it'),
                StreamFieldPanel('body_it')
            ],
            heading="Italien",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_fr'),
                StreamFieldPanel('body_fr')
            ],
            heading="French",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sv'),
                StreamFieldPanel('body_sv')
            ],
            heading="Swedish",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sl'),
                StreamFieldPanel('body_sl')
            ],
            heading="Slovene",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_da'),
                StreamFieldPanel('body_da')
            ],
            heading="Danish",
            classname="collapsible collapsed"
        )

    ]


class AboutPage(Page):
    pass
