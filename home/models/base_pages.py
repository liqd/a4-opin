from django.db import models
from wagtail import blocks as core_blocks
from wagtail.admin import panels
from wagtail.fields import StreamField
from wagtail.images import blocks as image_blocks
from wagtail.models import Page

from contrib import translations
from euth_wagtail.settings import LANGUAGES

from . import blocks


class HomePage(Page, metaclass=translations.TranslatedPageMetaclass):

    # Title
    translated_title = translations.TranslatedField(
        'title',
        models.CharField(
            max_length=255, blank=True, verbose_name="Header Title"
        ),
    )

    # Intro
    default_subtitle = (
        "Ever wondered how to get young people involved in politics online?"
        "OPIN, a European toolbox for youth eParticipation projects, shows "
        "you how."
    )

    translated_intro = translations.TranslatedField(
        'intro',
        models.CharField(
            max_length=255, blank=True, verbose_name="Subtitle",
            default=default_subtitle
        )
    )

    # Image
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
    block_types = [
        ('heading', core_blocks.CharBlock(classname="full title",
                                          icon="title")),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', blocks.InfoBlock()),
        ('video_block', blocks.VideoBlock()),
        ('news_block', blocks.NewsBlock()),
        ('rss_feed', blocks.RSSImportBlock()),
        ('column_block', blocks.ColumnBlock()),
        ('highlighted_column_block', blocks.HighlitedColumnBlock()),
        ('column_cta_block', blocks.ColumnCTABlock()),
        ('tile_column_block', blocks.TileLinkColumnBlock()),

    ]

    body = translations.TranslatedField(
        'body',
        StreamField(block_types, null=True, blank=True, use_json_field=True),
        overwrite_fallback={'blank': False},
    )

    class Meta:
        verbose_name = "Homepage"

    general_panels = [
        panels.FieldPanel('title', classname='title'),
        panels.FieldPanel('slug'),
        panels.FieldPanel('image'),
    ]

    content_panels = [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('title_' + lang_code),
                panels.FieldPanel('intro_' + lang_code),
                panels.FieldPanel('body_' + lang_code)
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]

    edit_handler = panels.TabbedInterface([
        panels.ObjectList(content_panels, heading='Content'),
        panels.ObjectList(general_panels, heading='General')
    ])

    parent_page_types = []
    subpage_types = [
        'home.SimplePage',
        'home.ManualsIndex'
    ]


class SimplePage(Page, metaclass=translations.TranslatedPageMetaclass):

    translated_title = translations.TranslatedField(
        'title',
        models.CharField(max_length=255, blank=True, verbose_name="Title"),
    )

    translated_intro = translations.TranslatedField(
        'intro',
        models.CharField(
            max_length=255, blank=True, verbose_name="Subtitle",
        )
    )

    intro_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Body
    block_types = [
        ('heading', core_blocks.CharBlock(classname="full title",
                                          icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', blocks.InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', blocks.WideImageBlock(icon="image")),
        ('images', blocks.InlineImagesBlock(icon="image")),
        ('contact_block', blocks.ContactBlock(icon="form")),
        ('accordion_block', blocks.AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', blocks.ImageTextBlockList()),
        ('rss_feed', blocks.RSSImportBlock()),
        ('highlighted_column_block', blocks.HighlitedColumnBlock()),
        ('column_cta_block', blocks.ColumnCTABlock()),
        ('tile_column_block', blocks.TileLinkColumnBlock()),
    ]

    body = translations.TranslatedField(
        'body',
        StreamField(
            block_types,
            null=True,
            blank=True,
            verbose_name='body',
            use_json_field=True),
    )

    general_panels = [
        panels.FieldPanel('title', classname='title'),
        panels.FieldPanel('slug'),
        panels.FieldPanel('intro_image')
    ]

    content_panels = [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('title_' + lang_code),
                panels.FieldPanel('intro_' + lang_code),
                panels.FieldPanel('body_' + lang_code)
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]

    edit_handler = panels.TabbedInterface([
        panels.ObjectList(content_panels, heading='Content'),
        panels.ObjectList(general_panels, heading='General')
    ])
