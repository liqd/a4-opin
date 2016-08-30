from __future__ import unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailadmin import edit_handlers
from wagtail.wagtailcore import blocks as core_blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailembeds import blocks as embed_blocks
from wagtail.wagtailimages import blocks as image_blocks
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets import blocks as snippet_blocks
from wagtail.wagtailsnippets.models import register_snippet

from contrib.translations.translations import TranslatedField

from euth.projects import models as prj_models

# Snippets
class RSSImport(models.Model):
    url = models.URLField(null=True, blank=True)

    rss_title = models.CharField(max_length=255)
    rss_title_de = models.CharField(max_length=255, blank=True)
    rss_title_it = models.CharField(max_length=255, blank=True)
    rss_title_fr = models.CharField(max_length=255, blank=True)
    rss_title_sv = models.CharField(max_length=255, blank=True)
    rss_title_sl = models.CharField(max_length=255, blank=True)
    rss_title_da = models.CharField(max_length=255, blank=True)

    translated_rss_title = TranslatedField(
        'rss_title_de',
        'rss_title_it',
        'rss_title',
        'rss_title_fr',
        'rss_title_sv',
        'rss_title_sl',
        'rss_title_da',
    )

    panels = [
        edit_handlers.FieldPanel('url'),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('rss_title'),
                edit_handlers.FieldPanel('rss_title_de'),
                edit_handlers.FieldPanel('rss_title_it'),
                edit_handlers.FieldPanel('rss_title_fr'),
                edit_handlers.FieldPanel('rss_title_sv'),
                edit_handlers.FieldPanel('rss_title_sl'),
                edit_handlers.FieldPanel('rss_title_da'),
            ],
            heading="Translations",
            classname="collapsible collapsed"
        )
    ]

    def __str__(self):
        return self.rss_title


class LinkFields(models.Model):
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+'
    )

    @property
    def link(self):
        return self.link_page.url

    panels = [
        edit_handlers.PageChooserPanel('link_page')
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
        edit_handlers.FieldPanel('menu_title'),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('menu_title_de'),
                edit_handlers.FieldPanel('menu_title_it'),
                edit_handlers.FieldPanel('menu_title_fr'),
                edit_handlers.FieldPanel('menu_title_sv'),
                edit_handlers.FieldPanel('menu_title_sl'),
                edit_handlers.FieldPanel('menu_title_da'),
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
    edit_handlers.FieldPanel('menu_name', classname='full title'),
    edit_handlers.InlinePanel('menu_items', label="Menu Items")
]

register_snippet(NavigationMenu)
register_snippet(RSSImport)


# Blocks
class RSSImportBlock(core_blocks.StructBlock):
    feed = snippet_blocks.SnippetChooserBlock(
        required=True, target_model=RSSImport)

    class Meta:
        template = 'home/blocks/rss_import_block.html'
        icon = 'snippet'
        label = 'RSS Import'


class InlineImageBlock(core_blocks.StructBlock):
    image = image_blocks.ImageChooserBlock()
    internal_link = core_blocks.PageChooserBlock(required=False)
    link_text = core_blocks.TextBlock(required=False)


class InlineImagesBlock(core_blocks.StructBlock):

    inline_images = core_blocks.ListBlock(InlineImageBlock())
    columns = core_blocks.ChoiceBlock(choices=[
        ('4', 'three columns'),
        ('6', 'two columns'),
    ], icon='cup', required=False, help_text='')

    class Meta:
        template = 'home/blocks/inline_images_block.html'
        icon = 'placeholder'
        label = 'Inline Images Block'


class CallToActionBlock(core_blocks.StructBlock):
    internal_link = core_blocks.PageChooserBlock(required=False)
    external_link = core_blocks.URLBlock(required=False)
    link_text = core_blocks.TextBlock(required=False)


class InfoBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title", required=False)
    image = image_blocks.ImageChooserBlock(required=False)
    text = core_blocks.RichTextBlock(required=False)
    button = CallToActionBlock(required=False)
    highlight = core_blocks.ChoiceBlock(choices=[
        ('', 'None'),
        ('highlight', 'Highlight'),
        ('boxed', 'Boxed'),
        ('boxed2', 'Boxed Variation'),
    ], icon='cup',
        required=False,
        help_text='How should this block be displayed?'
    )

    class Meta:
        template = 'home/blocks/info_block.html'
        icon = 'placeholder'
        label = 'Info Block'


class VideoBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title")
    video = embed_blocks.EmbedBlock()

    class Meta:
        template = 'home/blocks/video_block.html'
        icon = 'placeholder'
        label = 'Video Block'


class NewsBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title")
    news = core_blocks.CharBlock(classname="full title")

    class Meta:
        template = 'home/blocks/news_block.html'
        icon = 'placeholder'
        label = 'News Block'


class WideImageBlock(core_blocks.StructBlock):

    image = image_blocks.ImageChooserBlock()

    class Meta:
        template = 'home/blocks/wide_image_block.html'
        icon = 'placeholder'
        label = 'Wide Image Block'


class ContactBlock(core_blocks.StructBlock):

    title = core_blocks.CharBlock(classname="full title")
    name_label = core_blocks.CharBlock(classname="full title")
    email_label = core_blocks.CharBlock(classname="full title")
    subject_label = core_blocks.CharBlock(classname="full title")
    message_label = core_blocks.CharBlock(classname="full title")
    submit_label = core_blocks.CharBlock(classname="full title")

    class Meta:
        template = 'home/blocks/contact_block.html'
        icon = 'placeholder'
        label = 'Contact Block'


class AccordionItemBlock(core_blocks.StructBlock):
    title = core_blocks.TextBlock(required=False)
    content = core_blocks.RichTextBlock(required=False)


class AccordionBlock(core_blocks.StructBlock):

    accordion_items = core_blocks.ListBlock(AccordionItemBlock())

    class Meta:
        template = 'home/blocks/accordion_block.html'
        icon = 'placeholder'
        label = 'Accordion Block'


class ImageTextItemBlock(core_blocks.StructBlock):
    image = image_blocks.ImageChooserBlock()
    text = core_blocks.TextBlock()


class ImageTextBlockList(core_blocks.StructBlock):

    imageTextBlockList = core_blocks.ListBlock(ImageTextItemBlock())

    class Meta:
        template = 'home/blocks/imageTextBlockList_block.html'
        icon = 'placeholder'
        label = 'Image Text Block'


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
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
        ('rss_feed', RSSImportBlock()),
    ], null=True)

    body_de = StreamField([
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True)

    body_it = StreamField([
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True)

    body_fr = StreamField([
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True)

    body_sv = StreamField([
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True)

    body_sl = StreamField([
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True)

    body_da = StreamField([
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
        ('rss_feed', RSSImportBlock()),
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
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        ImageChooserPanel('image'),
    ]

    content_panels = [

        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_en'),
                edit_handlers.StreamFieldPanel('body_en')
            ],
            heading="English",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_de'),
                edit_handlers.StreamFieldPanel('body_de')
            ],
            heading="German",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_it'),
                edit_handlers.StreamFieldPanel('body_it')
            ],
            heading="Italien",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_fr'),
                edit_handlers.StreamFieldPanel('body_fr')
            ],
            heading="French",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_sv'),
                edit_handlers.StreamFieldPanel('body_sv')
            ],
            heading="Swedish",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_sl'),
                edit_handlers.StreamFieldPanel('body_sl')
            ],
            heading="Slovene",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_da'),
                edit_handlers.StreamFieldPanel('body_da')
            ],
            heading="Danish",
            classname="collapsible collapsed"
        )

    ]

    edit_handler = edit_handlers.TabbedInterface([
        edit_handlers.ObjectList(content_panels, heading='Content'),
        edit_handlers.ObjectList(general_panels, heading='General')
    ])

    parent_page_types = []
    subpage_types = [
        'home.SimplePage',
        'projects.ProjectsPage',
        'projects.OrganisationsPage',
    ]

    @property
    def featured_projects(self):
        return prj_models.Project.objects.featured()


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
        ('heading', core_blocks.CharBlock(
            classname="full title", icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', ImageTextBlockList()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True, verbose_name="body")

    body_de = StreamField([
        ('heading', core_blocks.CharBlock(
            classname="full title", icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', ImageTextBlockList()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True, verbose_name="body")

    body_it = StreamField([
        ('heading', core_blocks.CharBlock(
            classname="full title", icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', ImageTextBlockList()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True, verbose_name="body")

    body_fr = StreamField([
        ('heading', core_blocks.CharBlock(
            classname="full title", icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', ImageTextBlockList()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True, verbose_name="body")

    body_sv = StreamField([
        ('heading', core_blocks.CharBlock(
            classname="full title", icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', ImageTextBlockList()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True, verbose_name="body")

    body_sl = StreamField([
        ('heading', core_blocks.CharBlock(
            classname="full title", icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', ImageTextBlockList()),
        ('rss_feed', RSSImportBlock()),
    ], null=True, blank=True, verbose_name="body")

    body_da = StreamField([
        ('heading', core_blocks.CharBlock(
            classname="full title", icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', ImageTextBlockList()),
        ('rss_feed', RSSImportBlock()),
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
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        ImageChooserPanel('intro_image')
    ]

    content_panels = [
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_en'),
                edit_handlers.FieldPanel('intro_en'),
                edit_handlers.StreamFieldPanel('body_en')
            ],
            heading="English",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_de'),
                edit_handlers.FieldPanel('intro_de'),
                edit_handlers.StreamFieldPanel('body_de')
            ],
            heading="German",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_it'),
                edit_handlers.FieldPanel('intro_it'),
                edit_handlers.StreamFieldPanel('body_it')
            ],
            heading="Italien",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_fr'),
                edit_handlers.FieldPanel('intro_fr'),
                edit_handlers.StreamFieldPanel('body_fr')
            ],
            heading="French",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_sv'),
                edit_handlers.FieldPanel('intro_sv'),
                edit_handlers.StreamFieldPanel('body_sv')
            ],
            heading="Swedish",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_sl'),
                edit_handlers.FieldPanel('intro_sl'),
                edit_handlers.StreamFieldPanel('body_sl')
            ],
            heading="Slovene",
            classname="collapsible collapsed"
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('title_da'),
                edit_handlers.FieldPanel('intro_da'),
                edit_handlers.StreamFieldPanel('body_da')
            ],
            heading="Danish",
            classname="collapsible collapsed"
        )

    ]

    edit_handler = edit_handlers.TabbedInterface([
        edit_handlers.ObjectList(content_panels, heading='Content'),
        edit_handlers.ObjectList(general_panels, heading='General')
    ])
