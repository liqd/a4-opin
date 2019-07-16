from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin import edit_handlers
from wagtail.core.models import Orderable
from wagtail.images import edit_handlers as image_edit_handlers
from wagtail.snippets.models import register_snippet

from contrib import translations
from euth_wagtail.settings import LANGUAGES


class RSSImport(translations.TranslatedModel):
    url = models.URLField(null=True, blank=True)

    translated_rss_title = translations.TranslatedField(
        'rss_title',
        models.CharField(max_length=255, blank=True),
        overwrite_fallback={'blank': False},
    )

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
        null=True,
        on_delete=models.CASCADE
    )

    allowed_views = (
        ('organisation-list', 'List of Organisations'),
    )

    link_view = models.CharField(
        max_length=100,
        blank=True,
        choices=[
            (name, title) for name, title in allowed_views
        ]
    )

    def clean(self):
        if self.link_page and self.link_view:
            msg = 'Can only either link a view or a page.'
            raise ValidationError({
                'link_view': msg,
                'link_page': msg,
            })
        if not self.link_page and not self.link_view:
            msg = 'Specify either a link to a view or a page.'
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


class MenuItem(LinkFields, metaclass=translations.TranslatedModelMetaclass):
    translated_menu_title = translations.TranslatedField(
        'menu_title',
        models.CharField(max_length=255, blank=True),
        overwrite_fallback={'blank': False},
    )

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


class PageCollection(translations.TranslatedModel):
    title = translations.TranslatedField(
        'title',
        models.CharField(max_length=80, blank=True),
        overwrite_fallback={'blank': False},
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The Image that is shown on top of the page'
    )

    intro_text = translations.TranslatedField(
        'intro_text',
        models.CharField(max_length=250, blank=True),
        overwrite_fallback={'blank': False}
    )

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
    page_9 = models.ForeignKey('wagtailcore.Page', **args)
    page_10 = models.ForeignKey('wagtailcore.Page', **args)
    page_11 = models.ForeignKey('wagtailcore.Page', **args)
    page_12 = models.ForeignKey('wagtailcore.Page', **args)
    page_13 = models.ForeignKey('wagtailcore.Page', **args)
    page_14 = models.ForeignKey('wagtailcore.Page', **args)
    page_15 = models.ForeignKey('wagtailcore.Page', **args)
    page_16 = models.ForeignKey('wagtailcore.Page', **args)
    page_17 = models.ForeignKey('wagtailcore.Page', **args)
    page_count = 17

    panels = [
        edit_handlers.MultiFieldPanel([
            edit_handlers.FieldPanel(
                'title_{}'.format(lang_code)
            ) for lang_code, lang in LANGUAGES
        ],
            heading="Title",
        ),
        edit_handlers.MultiFieldPanel(
            [
                edit_handlers.FieldPanel(
                    'intro_text_{}'.format(lang_code)
                ) for lang_code, lang in LANGUAGES
            ],
            heading='intro_text'),
        edit_handlers.MultiFieldPanel([
            edit_handlers.PageChooserPanel(
                'page_{}'.format(x)
            ) for x in range(1, page_count + 1)
        ],
            classname="collapsible collapsed",
            heading="Pages",
        ),
        image_edit_handlers.ImageChooserPanel('image'),
    ]

    def __str__(self):
        return self.title

    @property
    def pages(self):
        return [
            getattr(self, 'page_{}'.format(count))
            for count in range(1, self.page_count + 1)
        ]


register_snippet(NavigationMenu)
register_snippet(RSSImport)
register_snippet(PageCollection)
