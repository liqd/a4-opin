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
from wagtail.wagtailadmin.edit_handlers import PageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from .blocks import InfoBlock
from .blocks import InlineImagesBlock
from .blocks import VideoBlock
from .blocks import NewsBlock
from .blocks import WideImageBlock
from .blocks import ContactBlock
from .blocks import AccordionBlock

# Pages


class HomePage(Page):

    # Title
    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_it = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_fr = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_sv = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_sl = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_da = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Header Image",
        help_text="The Image that is shown on top of the page"
    )

    # Body
    body_en = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
    ], null=True)

    body_de = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
    ], null=True, blank=True)

    body_it = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
    ], null=True, blank=True)

    body_fr = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
    ], null=True, blank=True)

    body_sv = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
    ], null=True, blank=True)

    body_sl = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
    ], null=True, blank=True)

    body_da = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
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

    general_panels = [
        FieldPanel('title', classname='title'),
        FieldPanel('slug'),
        ImageChooserPanel('image')
    ]

    content_panels = [

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
        ObjectList(general_panels, heading='General'),
        ObjectList(content_panels, heading='Content')
    ])

    parent_page_types = []
    subpage_types = ['home.SimplePage', 'projects.ProjectsPage']


class SimplePage(Page):

    # Title
    title_en = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_de = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_it = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_fr = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_sv = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_sl = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_da = models.CharField(
        max_length=255, blank=True, verbose_name="Title")

    intro_en = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_de = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_it = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_fr = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_sv = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_sl = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_da = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")

    intro_image = models.ForeignKey(
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
        ('rich_text', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down"))
    ], null=True, blank=True, verbose_name="body")

    body_de = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('rich_text', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down"))
    ], null=True, blank=True, verbose_name="body")

    body_it = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('rich_text', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down"))
    ], null=True, blank=True, verbose_name="body")

    body_fr = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('rich_text', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down"))
    ], null=True, blank=True, verbose_name="body")

    body_sv = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('rich_text', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down"))
    ], null=True, blank=True, verbose_name="body")

    body_sl = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('rich_text', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down"))
    ], null=True, blank=True, verbose_name="body")

    body_da = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon="title")),
        ('paragraph', blocks.TextBlock(icon="pilcrow")),
        ('rich_text', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down"))
    ], null=True, blank=True, verbose_name="body")

    translated_title = TranslatedField(
        'title_de',
        'title_it',
        'title_en',
        'title_fr',
        'title_sv',
        'title_sl',
        'title_da',
    )

    translated_intro = TranslatedField(
        'intro_de',
        'intro_it',
        'intro_en',
        'intro_fr',
        'intro_sv',
        'intro_sl',
        'intro_da',
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

    general_panels = [
        FieldPanel('title', classname='title'),
        FieldPanel('slug'),
        ImageChooserPanel('intro_image')
    ]

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('title_en'),
                FieldPanel('intro_en'),
                StreamFieldPanel('body_en')
            ],
            heading="English",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_de'),
                FieldPanel('intro_de'),
                StreamFieldPanel('body_de')
            ],
            heading="German",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_it'),
                FieldPanel('intro_it'),
                StreamFieldPanel('body_it')
            ],
            heading="Italien",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_fr'),
                FieldPanel('intro_fr'),
                StreamFieldPanel('body_fr')
            ],
            heading="French",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sv'),
                FieldPanel('intro_sv'),
                StreamFieldPanel('body_sv')
            ],
            heading="Swedish",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sl'),
                FieldPanel('intro_sl'),
                StreamFieldPanel('body_sl')
            ],
            heading="Slovene",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_da'),
                FieldPanel('intro_da'),
                StreamFieldPanel('body_da')
            ],
            heading="Danish",
            classname="collapsible collapsed"
        )

    ]

    edit_handler = TabbedInterface([
        ObjectList(general_panels, heading='General'),
        ObjectList(content_panels, heading='Content')
    ])


# Menu

class LinkFields(models.Model):
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+'
    )

    @property
    def link(self):
        return self.link_page.url

    panels = [
        PageChooserPanel('link_page')
    ]

    class Meta:
        abstract = True


class MenuItem(LinkFields):
    menu_title = models.CharField(max_length=255)
    menu_title_de = models.CharField(max_length=255, blank=True)
    menu_title_it = models.CharField(max_length=255, blank=True)
    menu_title_fr = models.CharField(max_length=255, blank=True)
    menu_title_sv = models.CharField(max_length=255, blank=True)
    menu_title_sl = models.CharField(max_length=255, blank=True)
    menu_title_da = models.CharField(max_length=255, blank=True)

    translated_menu_title = TranslatedField(
        'menu_title_de',
        'menu_title_it',
        'menu_title',
        'menu_title_fr',
        'menu_title_sv',
        'menu_title_sl',
        'menu_title_da',
    )

    @property
    def url(self):
        return self.link

    def __str__(self):
        return self.title

    panels = [
        FieldPanel('menu_title'),
        MultiFieldPanel(
            [
                FieldPanel('menu_title_de'),
                FieldPanel('menu_title_it'),
                FieldPanel('menu_title_fr'),
                FieldPanel('menu_title_sv'),
                FieldPanel('menu_title_sl'),
                FieldPanel('menu_title_da'),
            ],
            heading="Translations",
            classname="collapsible collapsed"
        )] + LinkFields.panels


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey('home.NavigationMenu', related_name='menu_items')


class NavigationMenu(ClusterableModel):

    menu_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.menu_name


NavigationMenu.panels = [
    FieldPanel('menu_name', classname='full title'),
    InlinePanel('menu_items', label="Menu Items")
]

register_snippet(NavigationMenu)
