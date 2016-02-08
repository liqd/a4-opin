from django.db import models
from wagtail.wagtailcore.models import Page
from contrib.translations.translations import TranslatedField
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel
from wagtail.wagtailadmin.edit_handlers import TabbedInterface
from wagtail.wagtailadmin.edit_handlers import ObjectList
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel


class Organisation(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('link'),
        ImageChooserPanel('logo')
    ]

    def __str__(self):
        return self.title

register_snippet(Organisation)


class ProjectPage(Page):

    # Image
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The image that is displayed on a projecttile in a project list'
    )

    organisation = models.ForeignKey(
        'projects.Organisation',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    COMMENTING_TEXT = 'Commenting Text'
    IDEA_COLLECTION = 'Idea Collection'
    MOBILE_POLLING = 'Mobile Polling'

    PROJECTTYPE_CHOICES = (
        (COMMENTING_TEXT, 'Commenting Text'),
        (IDEA_COLLECTION, 'Idea Collection'),
        (MOBILE_POLLING, 'Mobile Polling'),
    )

    # Type
    projecttype = models.CharField(max_length=255, choices=PROJECTTYPE_CHOICES)

    # Title
    title_en = models.CharField(max_length=255)
    title_de = models.CharField(max_length=255, blank=True)
    title_it = models.CharField(max_length=255, blank=True)
    title_fr = models.CharField(max_length=255, blank=True)
    title_sv = models.CharField(max_length=255, blank=True)
    title_sl = models.CharField(max_length=255, blank=True)
    title_da = models.CharField(max_length=255, blank=True)

    # teaser
    teaser_en = models.TextField()
    teaser_de = models.TextField(blank=True)
    teaser_it = models.TextField(blank=True)
    teaser_fr = models.TextField(blank=True)
    teaser_sv = models.TextField(blank=True)
    teaser_sl = models.TextField(blank=True)
    teaser_da = models.TextField(blank=True)

    teaser = TranslatedField(
        'teaser_de',
        'teaser_it',
        'teaser_en',
        'teaser_fr',
        'teaser_sv',
        'teaser_sl',
        'teaser_da',
    )

    translated_title = TranslatedField(
        'title_de',
        'title_it',
        'title',
        'title_fr',
        'title_sv',
        'title_sl',
        'title_da',
    )


class ProjectsPage(Page):
    title_en = models.CharField(max_length=255, blank=True)
    title_de = models.CharField(max_length=255, blank=True)
    title_it = models.CharField(max_length=255, blank=True)
    title_fr = models.CharField(max_length=255, blank=True)
    title_sv = models.CharField(max_length=255, blank=True)
    title_sl = models.CharField(max_length=255, blank=True)
    title_da = models.CharField(max_length=255, blank=True)

    @property
    def projects(self):
        projects = ProjectPage.objects.all()
        return projects

    translated_title = TranslatedField(
        'title_de',
        'title_it',
        'title_en',
        'title_fr',
        'title_sv',
        'title_sl',
        'title_da',
    )

    subpage_types = ['projects.AdhocracyProjectPage']

    general_panels = [
        FieldPanel('title', classname='title'),
        FieldPanel('slug'),
    ]

    content_panels = [
        FieldPanel('title_en'),
        FieldPanel('title_de'),
        FieldPanel('title_it'),
        FieldPanel('title_fr'),
        FieldPanel('title_sv'),
        FieldPanel('title_sl'),
        FieldPanel('title_da'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(general_panels, heading='General'),
        ObjectList(content_panels, heading='Content')
    ])


class AdhocracyProjectPage(ProjectPage):
    adhocracySDK_url = models.URLField()
    embedurl = models.URLField()
    widget = models.CharField(max_length=255)
    initial_url = models.CharField(max_length=255)
    autoresize = models.BooleanField(default=False)
    autourl = models.BooleanField(default=True)
    locale = models.CharField(max_length=2, blank=True)
    height = models.IntegerField()

    adhocracy_panel = [
        FieldPanel('adhocracySDK_url'),
        FieldPanel('embedurl'),
        FieldPanel('widget'),
        FieldPanel('initial_url'),
        FieldPanel('autoresize'),
        FieldPanel('autourl'),
        FieldPanel('locale'),
        FieldPanel('height'),
    ]

    general_panels = [
        FieldPanel('title', classname='title'),
        FieldPanel('slug'),
        ImageChooserPanel('image'),
        FieldPanel('projecttype'),
        SnippetChooserPanel('organisation', Organisation)
    ]

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('title_en'),
                FieldPanel('teaser_en'),
            ]
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_de'),
                FieldPanel('teaser_de')
            ],
            heading="German",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_it'),
                FieldPanel('teaser_it')
            ],
            heading="Italien",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_fr'),
                FieldPanel('teaser_fr')
            ],
            heading="French",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sv'),
                FieldPanel('teaser_sv')
            ],
            heading="Swedish",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sl'),
                FieldPanel('teaser_sl')
            ],
            heading="Slovene",
            classname="collapsible collapsed"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_da'),
                FieldPanel('teaser_da')
            ],
            heading="Danish",
            classname="collapsible collapsed"
        )

    ]
    edit_handler = TabbedInterface([
        ObjectList(general_panels, heading='General'),
        ObjectList(content_panels, heading='Content'),

    ])
