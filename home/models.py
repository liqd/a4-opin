from __future__ import unicode_literals

from django.db import models
from contrib.translations.translations import TranslatedField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import StructBlock, TextBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface
from wagtail.wagtailadmin.edit_handlers import ObjectList

from modelcluster.fields import ParentalKey

# Blocks, using StreamField

class ImageTextBlock(blocks.StructBlock):

    left_column = ImageChooserBlock()
    right_column = TextBlock()

    class Meta:
        template = 'home/blocks/m_t_block.html'
        icon = 'placeholder'
        label = 'Image Text Block'


class TextImageBlock(blocks.StructBlock):

    left_column = TextBlock()
    right_column = ImageChooserBlock()

    class Meta:
        template = 'home/blocks/m_t_block.html'
        icon = 'placeholder'
        label = 'Text Image Block'


class EmbedTextBlock(blocks.StructBlock):

    left_column = EmbedBlock()
    right_column = TextBlock()

    class Meta:
        template = 'home/blocks/m_t_block.html'
        icon = 'placeholder'
        label = 'Video Text Block'


class TextEmbedBlock(blocks.StructBlock):

    left_column = TextBlock()
    right_column = EmbedBlock()

    class Meta:
        template = 'home/blocks/m_t_block.html'
        icon = 'placeholder'
        label = 'Text Video Block'


class ThreeImagesBlock(blocks.StructBlock):

    left_image = ImageChooserBlock()
    left_image_text = TextBlock()
    middle_image = ImageChooserBlock()
    middle_image_text = TextBlock()
    right_image = ImageChooserBlock()
    right_image_text = TextBlock()

    class Meta:
        template = 'home/blocks/3_im_block.html'
        icon = 'placeholder'
        label = 'Three Images Block'


class CollapsibleTextBlock(blocks.StructBlock):

    heading = TextBlock()
    text = TextBlock()

    class Meta:
        template = 'home/blocks/collaps_t_block.html'
        icon = 'arrows-up-down'
        label = 'Collapsible Text'


class CarouselItem(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField("Embed URL", blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
    ]

    class Meta:
        abstract = True


class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.HomePage', related_name='carousel_items')


# Pages

class HomePage(Page):

    # Title
    title_en = models.CharField(max_length=255, blank=True)
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
        ('image_text', ImageTextBlock()),
        ('text_image', TextImageBlock()),
        ('embed_text', EmbedTextBlock()),
        ('text_embed', TextEmbedBlock()),
        ('three_images', ThreeImagesBlock()),
        ('collapsible_text', CollapsibleTextBlock()),
    ], null=True)

    body_de = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('image_text', ImageTextBlock()),
        ('text_image', TextImageBlock()),
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

    carousel_panels = [
    InlinePanel('carousel_items', label="Carousel items"),
    ]

    content_panels = [

    FieldPanel('title'),
    MultiFieldPanel(
        [
            StreamFieldPanel('body_en')
        ],
        heading="English",
        classname="collapsible collapsed"
    ),
    MultiFieldPanel(
        [
            StreamFieldPanel('body_de')
        ],
        heading="German",
        classname="collapsible collapsed"
    ),
    MultiFieldPanel(
        [
            StreamFieldPanel('body_it')
        ],
        heading="Italien",
        classname="collapsible collapsed"
    ),
    MultiFieldPanel(
        [
            StreamFieldPanel('body_fr')
        ],
        heading="French",
        classname="collapsible collapsed"
    ),
    MultiFieldPanel(
        [
            StreamFieldPanel('body_sv')
        ],
        heading="Swedish",
        classname="collapsible collapsed"
    ),
    MultiFieldPanel(
        [
            StreamFieldPanel('body_sl')
        ],
        heading="Slovene",
        classname="collapsible collapsed"
    ),
    MultiFieldPanel(
        [
            StreamFieldPanel('body_da')
        ],
        heading="Danish",
        classname="collapsible collapsed"
    )

    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(carousel_panels, heading='Carousel'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])


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
        ('image_text', ImageTextBlock()),
        ('text_image', TextImageBlock()),
        ('embed_text', EmbedTextBlock()),
        ('text_embed', TextEmbedBlock()),
        ('three_images', ThreeImagesBlock()),
        ('collapsible_text', CollapsibleTextBlock()),
    ], null=True)

    body_de = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('image_text', ImageTextBlock()),
        ('text_image', TextImageBlock()),
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
