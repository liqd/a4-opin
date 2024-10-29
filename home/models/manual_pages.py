from django.db import models
from wagtail import blocks as core_blocks
from wagtail.admin import panels
from wagtail.fields import StreamField
from wagtail.images import blocks as image_blocks
from wagtail.models import Page
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
            verbose_name="body",
            use_json_field=True
        ),
    )

    subpage_types = [
        'home.ManualsSectionPage', 'home.ManualsDetailPage'
    ]

    content_panels = [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('title_' + lang_code),
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]

    general_panels = [
        panels.TitleFieldPanel('title', classname='title'),
        panels.FieldPanel('slug'),
    ]

    edit_handler = panels.TabbedInterface([
        panels.ObjectList(content_panels, heading='Content'),
        panels.ObjectList(general_panels, heading='General')
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
    ], use_json_field=True)

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
        panels.TitleFieldPanel('title', classname='title'),
        panels.FieldPanel('slug'),
        panels.FieldPanel('color'),
        panels.FieldPanel('image'),
        panels.FieldPanel('document')
    ]

    content_panels = [
        panels.FieldPanel('body'),
    ] + [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('title_' + lang_code),
                panels.FieldPanel('description_' + lang_code),
            ],
            heading=lang,
            classname="collapsible collapsed"
        ) for lang_code, lang in LANGUAGES
    ]

    edit_handler = panels.TabbedInterface([
        panels.ObjectList(content_panels, heading='Content'),
        panels.ObjectList(general_panels, heading='General')
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
            verbose_name="body",
            use_json_field=True))

    content_panels = [
        panels.MultiFieldPanel(
            [
                panels.FieldPanel('title_' + lang_code),
                panels.FieldPanel('description_' + lang_code),
                panels.FieldPanel('body_' + lang_code),
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
        panels.TitleFieldPanel('title', classname='title'),
        panels.FieldPanel('slug'),
        panels.FieldPanel('color'),
        panels.FieldPanel('image'),
    ]

    edit_handler = panels.TabbedInterface([
        panels.ObjectList(content_panels, heading='Content'),
        panels.ObjectList(general_panels, heading='General')
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
