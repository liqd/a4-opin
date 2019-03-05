from django.db import models
from wagtail.admin import edit_handlers
from wagtail.core import blocks as core_blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images import blocks as image_blocks
from wagtail.images import edit_handlers as image_edit_handlers

from adhocracy4.projects import models as prj_models
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

    videoplayer_url = models.URLField()

    # Body
    block_types = [
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', blocks.InfoBlock()),
        ('video_block', blocks.VideoBlock()),
        ('news_block', blocks.NewsBlock()),
        ('rss_feed', blocks.RSSImportBlock()),
        ('column_block', blocks.ColumnBlock()),
    ]

    body = translations.TranslatedField(
        'body',
        StreamField(block_types, null=True, blank=True),
        overwrite_fallback={'blank': False},
    )

    class Meta:
        verbose_name = "Homepage"

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        image_edit_handlers.ImageChooserPanel('image'),
        edit_handlers.FieldPanel('videoplayer_url'),
    ]

    content_panels = [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_' + lang_code),
                edit_handlers.FieldPanel('intro_' + lang_code),
                edit_handlers.StreamFieldPanel('body_' + lang_code)
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]

    edit_handler = edit_handlers.TabbedInterface([
        edit_handlers.ObjectList(content_panels, heading='Content'),
        edit_handlers.ObjectList(general_panels, heading='General')
    ])

    parent_page_types = []
    subpage_types = [
        'home.SimplePage',
        'home.ManualsIndex'
    ]

    @property
    def featured_projects(self):
        return prj_models.Project.objects.featured()


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
    ]

    body = translations.TranslatedField(
        'body',
        StreamField(block_types, null=True, blank=True, verbose_name='body'),
    )

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        image_edit_handlers.ImageChooserPanel('intro_image')
    ]

    content_panels = [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_' + lang_code),
                edit_handlers.FieldPanel('intro_' + lang_code),
                edit_handlers.StreamFieldPanel('body_' + lang_code)
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]

    edit_handler = edit_handlers.TabbedInterface([
        edit_handlers.ObjectList(content_panels, heading='Content'),
        edit_handlers.ObjectList(general_panels, heading='General')
    ])
