from django.db import models
from wagtail.admin import edit_handlers
from wagtail.core import blocks as core_blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.documents import edit_handlers as doc_edit_handlers
from wagtail.images import blocks as image_blocks
from wagtail.images import edit_handlers as image_edit_handlers
from wagtail.snippets import blocks as snippet_blocks

from contrib import translations
from euth_wagtail.settings import LANGUAGES

from . import blocks
from .snippets import PageCollection


class ManualsIndex(Page, metaclass=translations.TranslatedPageMetaclass):

    translated_title = translations.TranslatedField(
        'title',
        models.CharField(max_length=150, blank=True, verbose_name="Title"),
    )

    block_types = [
        ('heading', core_blocks.CharBlock(classname="full title",
                                          icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', blocks.InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', blocks.WideImageBlock(icon="image")),
        ('images', blocks.InlineImagesBlock(icon="image")),
        ('image_text_block_list', blocks.ImageTextBlockList()),
    ]

    body = translations.TranslatedField(
        'body',
        StreamField(block_types, null=True, blank=True, verbose_name="body"),
    )

    subpage_types = [
        'home.ManualsSectionPage', 'home.ManualsDetailPage'
    ]

    content_panels = [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_' + lang_code),
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
    ]

    edit_handler = edit_handlers.TabbedInterface([
        edit_handlers.ObjectList(content_panels, heading='Content'),
        edit_handlers.ObjectList(general_panels, heading='General')
    ])

    @property
    def subpages(self):
        return self.get_children().live().specific()


class ManualsSectionPage(Page, metaclass=translations.TranslatedPageMetaclass):

    translated_title = translations.TranslatedField(
        'title',
        models.CharField(max_length=150, blank=True, verbose_name="Title"),
    )

    description = translations.TranslatedField(
        'description',
        models.CharField(
            max_length=260, blank=True, verbose_name="Description"
        )
    )

    body = StreamField([
        (
            'snippet', snippet_blocks.SnippetChooserBlock(
                required=False,
                target_model=PageCollection,
                template='home/blocks/page_collection_block.html'
            )
        )
    ])

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    document = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
    )

    colors = (
        ('blue', 'Blue'),
        ('orange', 'Orange'),
        ('turquoise', 'Turquoise'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
    )

    color = models.CharField(
        choices=colors,
        max_length=9,
        blank=False,
        default='blue'
    )

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        edit_handlers.FieldPanel('color'),
        image_edit_handlers.ImageChooserPanel('image'),
        doc_edit_handlers.DocumentChooserPanel('document')
    ]

    content_panels = [
        edit_handlers.StreamFieldPanel('body'),
    ] + [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_' + lang_code),
                edit_handlers.FieldPanel('description_' + lang_code),
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]

    edit_handler = edit_handlers.TabbedInterface([
        edit_handlers.ObjectList(content_panels, heading='Content'),
        edit_handlers.ObjectList(general_panels, heading='General')
    ])

    parent_page_types = [
        'home.ManualsIndex'
    ]
    subpage_types = [
        'home.ManualsDetailPage'
    ]


class ManualsDetailPage(Page, metaclass=translations.TranslatedPageMetaclass):
    subpage_types = []
    parent_page_types = [
        'home.ManualsSectionPage',
        'home.ManualsIndex'
    ]

    # Title
    translated_title = translations.TranslatedField(
        'title',
        models.CharField(max_length=150, blank=True, verbose_name="Title")
    )

    # Subtitle (Field named description as in ManualsSectionPage)
    description = translations.TranslatedField(
        'description',
        models.CharField(
            max_length=260, blank=True, verbose_name="Subtitle"
        )
    )

    # Body
    block_types = [
        ('heading', core_blocks.CharBlock(classname="full title",
                                          icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('video_block', blocks.VideoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('accordion_block', blocks.AccordionBlock(icon="collapse-down")),
    ]

    body = translations.TranslatedField(
        'body',
        StreamField(block_types, null=True, blank=True, verbose_name="body")
    )

    content_panels = [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_' + lang_code),
                edit_handlers.FieldPanel('description_' + lang_code),
                edit_handlers.StreamFieldPanel('body_' + lang_code),
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    colors = (
        ('blue', 'Blue'),
        ('orange', 'Orange'),
        ('turquoise', 'Turquoise'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
    )

    color = models.CharField(
        choices=colors,
        max_length=9,
        blank=True,
        default='blue'
    )

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        edit_handlers.FieldPanel('color'),
        image_edit_handlers.ImageChooserPanel('image'),
    ]

    edit_handler = edit_handlers.TabbedInterface([
        edit_handlers.ObjectList(content_panels, heading='Content'),
        edit_handlers.ObjectList(general_panels, heading='General')
    ])

    def get_template(self, request, **kwargs):
        # only render detail page with sidebar if there's a section
        if self.parent_page.__class__.__name__ == 'ManualsSectionPage':
            return 'home/manuals_detail_page_sections.html'
        else:
            return 'home/manuals_detail_page.html'

    @property
    def parent_page(self):
        return self.get_ancestors().live().specific().last()
