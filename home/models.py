from __future__ import unicode_literals

from operator import attrgetter

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
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

from adhocracy4.projects import models as prj_models
from contrib.translations.translations import TranslatedField
from euth.organisations import urls as org_urls
from euth_wagtail.settings import LANGUAGES


# Snippets
class RSSImport(models.Model):
    url = models.URLField(null=True, blank=True)

    rss_title_en = models.CharField(max_length=255)
    rss_title_de = models.CharField(max_length=255, blank=True)
    rss_title_it = models.CharField(max_length=255, blank=True)
    rss_title_fr = models.CharField(max_length=255, blank=True)
    rss_title_sv = models.CharField(max_length=255, blank=True)
    rss_title_sl = models.CharField(max_length=255, blank=True)
    rss_title_da = models.CharField(max_length=255, blank=True)
    rss_title_uk = models.CharField(max_length=255, blank=True)
    rss_title_el = models.CharField(max_length=255, blank=True)
    rss_title_ru = models.CharField(max_length=255, blank=True)
    rss_title_ka = models.CharField(max_length=255, blank=True)
    rss_title_mk = models.CharField(max_length=255, blank=True)
    rss_title_mt = models.CharField(max_length=255, blank=True)

    translated_rss_title = TranslatedField('rss_title')

    panels = [
        edit_handlers.FieldPanel('url'),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('rss_title_' + lang_code)
                for lang_code, _language in LANGUAGES
            ],
            heading="Translations",
            classname="collapsible collapsed"
        )
    ]

    def __str__(self):
        return self.rss_title_en


class LinkFields(models.Model):

    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+',
        blank=True,
        null=True
    )

    allowed_views = (
        (org_urls, 'organisation-list', _('List of Organisations')),
    )

    link_view = models.CharField(
        max_length=100,
        blank=True,
        choices=[
            (name, title) for urlconfig, name, title in allowed_views
            if name in map(attrgetter('name'), urlconfig.urlpatterns)
        ]
    )

    def clean(self):
        if self.link_page and self.link_view:
            msg = _('Can only either link a view or a page.')
            raise ValidationError({
                'link_view': msg,
                'link_page': msg,
            })
        if not self.link_page and not self.link_view:
            msg = _('Specify either a link to a view or a page.')
            raise ValidationError({
                'link_view': msg,
                'link_page': msg,
            })

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return reverse(self.link_view)

    panels = [
        edit_handlers.PageChooserPanel('link_page'),
        edit_handlers.FieldPanel('link_view'),
    ]

    class Meta:
        abstract = True


class MenuItem(LinkFields):
    menu_title_en = models.CharField(max_length=255)
    menu_title_de = models.CharField(max_length=255, blank=True)
    menu_title_it = models.CharField(max_length=255, blank=True)
    menu_title_fr = models.CharField(max_length=255, blank=True)
    menu_title_sv = models.CharField(max_length=255, blank=True)
    menu_title_sl = models.CharField(max_length=255, blank=True)
    menu_title_da = models.CharField(max_length=255, blank=True)
    menu_title_uk = models.CharField(max_length=255, blank=True)
    menu_title_el = models.CharField(max_length=255, blank=True)
    menu_title_ru = models.CharField(max_length=255, blank=True)
    menu_title_ka = models.CharField(max_length=255, blank=True)
    menu_title_mk = models.CharField(max_length=255, blank=True)
    menu_title_mt = models.CharField(max_length=255, blank=True)

    translated_menu_title = TranslatedField('menu_title')

    @property
    def url(self):
        return self.link

    def __str__(self):
        return self.title

    panels = [
        edit_handlers.FieldPanel('menu_title_en'),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel('menu_title_' + lang_code)
                for lang_code, _language in LANGUAGES
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


class PageCollection(models.Model):
    title = TranslatedField('title')
    title_en = models.CharField(max_length=80)
    title_de = models.CharField(max_length=80, blank=True)
    title_it = models.CharField(max_length=80, blank=True)
    title_fr = models.CharField(max_length=80, blank=True)
    title_sv = models.CharField(max_length=80, blank=True)
    title_sl = models.CharField(max_length=80, blank=True)
    title_da = models.CharField(max_length=80, blank=True)
    title_uk = models.CharField(max_length=80, blank=True)
    title_el = models.CharField(max_length=80, blank=True)
    title_ru = models.CharField(max_length=80, blank=True)
    title_ka = models.CharField(max_length=80, blank=True)
    title_mk = models.CharField(max_length=80, blank=True)
    title_mt = models.CharField(max_length=80, blank=True)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The Image that is shown on top of the page'
    )

    intro_text = models.CharField(max_length=250, blank=True)

    args = {
        'on_delete': models.SET_NULL,
        'null': True,
        'blank': True,
        'related_name': '+'
    }

    page_1 = models.ForeignKey('wagtailcore.Page', **args)
    page_2 = models.ForeignKey('wagtailcore.Page', **args)
    page_3 = models.ForeignKey('wagtailcore.Page', **args)
    page_4 = models.ForeignKey('wagtailcore.Page', **args)
    page_5 = models.ForeignKey('wagtailcore.Page', **args)
    page_6 = models.ForeignKey('wagtailcore.Page', **args)
    page_7 = models.ForeignKey('wagtailcore.Page', **args)
    page_8 = models.ForeignKey('wagtailcore.Page', **args)

    panels = [
        edit_handlers.MultiFieldPanel([
            edit_handlers.FieldPanel(
                'title_{}'.format(lang_code)
            ) for lang_code, lang in LANGUAGES
        ],
            heading="Title",
        ),
        edit_handlers.FieldPanel('intro_text'),
        edit_handlers.MultiFieldPanel([
            edit_handlers.PageChooserPanel(
                'page_{}'.format(x)
            ) for x in range(1, 8)
        ],
            classname="collapsible collapsed",
            heading="Pages",
        ),
        ImageChooserPanel('image'),
     ]

    def __str__(self):
        return self.title

    @property
    def pages(self):
        return [self.page_1, self.page_2, self.page_3, self.page_4,
                self.page_5, self.page_6, self.page_7, self.page_8]


register_snippet(NavigationMenu)
register_snippet(RSSImport)
register_snippet(PageCollection)


# Blocks
class RSSImportBlock(core_blocks.StructBlock):
    feed = snippet_blocks.SnippetChooserBlock(
        required=True, target_model=RSSImport)

    class Meta:
        template = 'home/blocks/rss_import_block.html'
        icon = 'snippet'
        label = 'RSS Import'


class PageCollectionBlock(core_blocks.StructBlock):
    page_collection = snippet_blocks.SnippetChooserBlock(
        required=False, target_model=PageCollection)

    class Meta:
        template = 'home/blocks/page_collection_block.html'
        icon = 'snippet'
        label = 'Page Collection'


class InlineImageBlock(core_blocks.StructBlock):
    image = image_blocks.ImageChooserBlock()
    internal_link = core_blocks.PageChooserBlock(required=False)
    external_link = core_blocks.URLBlock(required=False)
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
        ('highlight', 'Highlight (blue)'),
        ('boxed', 'Boxed'),
        ('boxed2', 'Boxed Variation'),
        ('highlight-purple', 'Highlight (purple)')
    ], icon='cup',
        required=False,
        help_text='How should this block be displayed?'
    )
    alignment = core_blocks.ChoiceBlock(
        choices=[
            ('vertical', 'vertical'),
            ('horizontal', 'horizontal'),
        ],
        icon='cup',
        default='vertical',
        help_text='How should the text and image be aligned?'
    )

    class Meta:
        template = 'home/blocks/info_block.html'
        icon = 'placeholder'
        label = 'Info Block'


class ColumnBlock(core_blocks.StructBlock):
    title_col1 = core_blocks.CharBlock(classname="full title", required=False)
    image_col1 = image_blocks.ImageChooserBlock(required=False)
    text_col1 = core_blocks.RichTextBlock(required=False)

    title_col2 = core_blocks.CharBlock(classname="full title", required=False)
    image_col2 = image_blocks.ImageChooserBlock(required=False)
    text_col2 = core_blocks.RichTextBlock(required=False)

    title_col3 = core_blocks.CharBlock(classname="full title", required=False)
    image_col3 = image_blocks.ImageChooserBlock(required=False)
    text_col3 = core_blocks.RichTextBlock(required=False)

    class Meta:
        template = 'home/blocks/column_block.html'
        icon = 'placeholder'
        label = 'Column Block'


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
    title_uk = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_el = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_ru = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_ka = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_mk = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")
    title_mt = models.CharField(
        max_length=255, blank=True, verbose_name="Header Title")

    default_subtitle = (
        "Ever wondered how to get young people involved in politics online?"
        "OPIN, a European toolbox for youth eParticipation projects, shows "
        "you how."
    )

    intro_en = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_de = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_it = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_fr = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_sv = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_sl = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_da = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_uk = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_el = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_ru = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_ka = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_mk = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)
    intro_mt = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle",
        default=default_subtitle)

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
        ('info_block', InfoBlock()),
        ('video_block', VideoBlock()),
        ('news_block', NewsBlock()),
        ('rss_feed', RSSImportBlock()),
        ('column_block', ColumnBlock()),
    ]
    body_en = StreamField(block_types, null=True)
    body_de = StreamField(block_types, null=True, blank=True)
    body_it = StreamField(block_types, null=True, blank=True)
    body_fr = StreamField(block_types, null=True, blank=True)
    body_sv = StreamField(block_types, null=True, blank=True)
    body_sl = StreamField(block_types, null=True, blank=True)
    body_da = StreamField(block_types, null=True, blank=True)
    body_uk = StreamField(block_types, null=True, blank=True)
    body_el = StreamField(block_types, null=True, blank=True)
    body_ru = StreamField(block_types, null=True, blank=True)
    body_ka = StreamField(block_types, null=True, blank=True)
    body_mk = StreamField(block_types, null=True, blank=True)
    body_mt = StreamField(block_types, null=True, blank=True)

    body = TranslatedField('body')

    translated_title = TranslatedField('title')
    translated_intro = TranslatedField('intro')

    class Meta:
        verbose_name = "Homepage"

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        ImageChooserPanel('image'),
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
    title_uk = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_el = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_ru = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_ka = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_mk = models.CharField(
        max_length=255, blank=True, verbose_name="Title")
    title_mt = models.CharField(
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
    intro_uk = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_el = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_ru = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_ka = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_mk = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")
    intro_mt = models.CharField(
        max_length=255, blank=True, verbose_name="Subtitle")

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
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('contact_block', ContactBlock(icon="form")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
        ('image_text_block_list', ImageTextBlockList()),
        ('rss_feed', RSSImportBlock()),
    ]

    body_en = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_de = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_it = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_fr = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_sv = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_sl = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_da = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_uk = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_el = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_ru = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_ka = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_mk = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_mt = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")

    translated_title = TranslatedField('title')

    translated_intro = TranslatedField('intro')

    body = TranslatedField('body')

    general_panels = [
        edit_handlers.FieldPanel('title', classname='title'),
        edit_handlers.FieldPanel('slug'),
        ImageChooserPanel('intro_image')
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


class ManualsIndex(Page):
    translated_title = TranslatedField('title')
    title_en = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_de = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_it = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_fr = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_sv = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_sl = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_da = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_uk = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_el = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_ru = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_ka = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_mk = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_mt = models.CharField(
        max_length=150, blank=True, verbose_name="Title")

    block_types = [
        ('heading', core_blocks.CharBlock(classname="full title",
                                          icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('info_block', InfoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('wide_image', WideImageBlock(icon="image")),
        ('images', InlineImagesBlock(icon="image")),
        ('image_text_block_list', ImageTextBlockList()),
    ]

    body = TranslatedField('body')
    body_en = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_de = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_it = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_fr = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_sv = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_sl = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_da = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_uk = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_el = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_ru = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_ka = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_mk = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_mt = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")

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


class ManualsSectionPage(Page):
    # Title
    translated_title = TranslatedField('title')
    title_en = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_de = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_it = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_fr = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_sv = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_sl = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_da = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_uk = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_el = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_ru = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_ka = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_mk = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_mt = models.CharField(
        max_length=150, blank=True, verbose_name="Title")

    description = TranslatedField('description')
    description_en = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_de = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_it = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_fr = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_sv = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_sl = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_da = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_uk = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_el = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_ru = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_ka = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_mk = models.CharField(
        max_length=260, blank=True, verbose_name="Description")
    description_mt = models.CharField(
        max_length=260, blank=True, verbose_name="Description")

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
        ImageChooserPanel('image'),
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


class ManualsDetailPage(Page):
    subpage_types = []
    parent_page_types = [
        'home.ManualsSectionPage',
        'home.ManualsIndex'
    ]

    # Title
    translated_title = TranslatedField('title')
    title_en = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_de = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_it = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_fr = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_sv = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_sl = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_da = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_uk = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_el = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_ru = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_ka = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_mk = models.CharField(
        max_length=150, blank=True, verbose_name="Title")
    title_mt = models.CharField(
        max_length=150, blank=True, verbose_name="Title")

    # Subtitle
    subtitle = TranslatedField('subtitle')
    subtitle_en = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_de = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_it = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_fr = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_sv = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_sl = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_da = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_uk = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_el = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_ru = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_ka = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_mk = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")
    subtitle_mt = models.CharField(
        max_length=150, blank=True, verbose_name="Subtitle")

    # Body
    body = TranslatedField('body')
    block_types = [
        ('heading', core_blocks.CharBlock(classname="full title",
                                          icon="title")),
        ('paragraph', core_blocks.TextBlock(icon="pilcrow")),
        ('rich_text', core_blocks.RichTextBlock(icon="pilcrow")),
        ('video_block', VideoBlock()),
        ('image', image_blocks.ImageChooserBlock(icon="image")),
        ('accordion_block', AccordionBlock(icon="collapse-down")),
    ]

    body_en = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_de = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_it = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_fr = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_sv = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_sl = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_da = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_uk = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_el = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_ru = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_ka = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_mk = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")
    body_mt = StreamField(block_types, null=True,
                          blank=True, verbose_name="body")

    content_panels = [
        edit_handlers.MultiFieldPanel([
                edit_handlers.FieldPanel('title_' + lang_code),
                edit_handlers.FieldPanel('subtitle_' + lang_code),
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
        ImageChooserPanel('image'),
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
