from __future__ import unicode_literals

from django.db import models
from contrib.translations.translations import TranslatedField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import StructBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel


class HomePage(Page):
    pass

class TwoColumnBlock(blocks.StructBlock):

    left_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.TextBlock()),
            ('image', ImageChooserBlock()),
        ], icon='arrow-left', label='Left column content')

    right_column = blocks.StreamBlock([
            ('heading', blocks.CharBlock(classname="full title")),
            ('paragraph', blocks.TextBlock()),
            ('image', ImageChooserBlock()),
        ], icon='arrow-right', label='Right column content')

    class Meta:
        template = 'home/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'



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
        ('two_columns', TwoColumnBlock()),
    ], null=True)

    body_de = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('two_columns', TwoColumnBlock()),
    ], null=True, blank=True)

    body_it = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('two_columns', TwoColumnBlock()),
    ], null=True, blank=True)

    body_fr = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('two_columns', TwoColumnBlock()),
    ], null=True, blank=True)

    body_sv = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('two_columns', TwoColumnBlock()),
    ], null=True, blank=True)

    body_sl = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('two_columns', TwoColumnBlock()),
    ], null=True, blank=True)

    body_da = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('two_columns', TwoColumnBlock()),
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
         heading = "Slovene",
         classname = "collapsible collapsed"
    ),
    MultiFieldPanel (
        [
            FieldPanel('title_da'),
            StreamFieldPanel('body_da')
        ],
         heading = "Danish",
         classname = "collapsible collapsed"
    )

]
