from django.db import models
from django_countries.fields import CountryField
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
                                                MultiFieldPanel, ObjectList,
                                                TabbedInterface)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from contrib.translations.translations import TranslatedField


class OrganisationPage(Page):
    link = models.URLField()
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    country = CountryField(help_text='Where is the' +
                                     'Organisation located')

    # Title
    name_en = models.CharField(max_length=255, blank=True)
    name_de = models.CharField(max_length=255, blank=True)
    name_it = models.CharField(max_length=255, blank=True)
    name_fr = models.CharField(max_length=255, blank=True)
    name_sv = models.CharField(max_length=255, blank=True)
    name_sl = models.CharField(max_length=255, blank=True)
    name_da = models.CharField(max_length=255, blank=True)

    # Teaser
    teaser_en = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_de = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_it = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_fr = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_sv = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_sl = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_da = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")

    # Description
    description_en = RichTextField(blank=True)
    description_de = RichTextField(blank=True)
    description_it = RichTextField(blank=True)
    description_fr = RichTextField(blank=True)
    description_sv = RichTextField(blank=True)
    description_sl = RichTextField(blank=True)
    description_da = RichTextField(blank=True)

    description = TranslatedField(
        'description_de',
        'description_it',
        'description_en',
        'description_fr',
        'description_sv',
        'description_sl',
        'description_da',
    )

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
        'name_de',
        'name_it',
        'name_en',
        'name_fr',
        'name_sv',
        'name_sl',
        'name_da',
    )

    projects_panels = [
        InlinePanel('organisation_projects', label="projects")
    ]

    general_panels = [
        FieldPanel('title', classname="title"),
        FieldPanel('slug'),
        FieldPanel('link'),
        FieldPanel('country'),
        ImageChooserPanel('logo'),
    ]

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('name_en'),
                FieldPanel('teaser_en'),
                FieldPanel('description_en')
            ],
            heading="English",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('name_de'),
                FieldPanel('teaser_de'),
                FieldPanel('description_de')
            ],
            heading="German",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('name_it'),
                FieldPanel('teaser_it'),
                FieldPanel('description_it')
            ],
            heading="Italien",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('name_fr'),
                FieldPanel('teaser_fr'),
                FieldPanel('description_fr')
            ],
            heading="French",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('name_sv'),
                FieldPanel('teaser_sv'),
                FieldPanel('description_sv')
            ],
            heading="Swedish",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('name_sl'),
                FieldPanel('teaser_sl'),
                FieldPanel('description_sl')
            ],
            heading="Slovene",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('name_da'),
                FieldPanel('teaser_da'),
                FieldPanel('description_da')
            ],
            heading="Danish",
            classname="collapsible"
        )
    ]

    edit_handler = TabbedInterface([
        ObjectList(general_panels, heading='General'),
        ObjectList(content_panels, heading='Content'),
        ObjectList(projects_panels, heading='Projects')
    ])


class OrganisationsPage(Page):
    title_en = models.CharField(max_length=255, blank=True)
    title_de = models.CharField(max_length=255, blank=True)
    title_it = models.CharField(max_length=255, blank=True)
    title_fr = models.CharField(max_length=255, blank=True)
    title_sv = models.CharField(max_length=255, blank=True)
    title_sl = models.CharField(max_length=255, blank=True)
    title_da = models.CharField(max_length=255, blank=True)

    @property
    def organisations(self):
        organisations = OrganisationPage.objects.all()
        return organisations

    translated_title = TranslatedField(
        'title_de',
        'title_it',
        'title_en',
        'title_fr',
        'title_sv',
        'title_sl',
        'title_da',
    )

    subpage_types = ['projects.OrganisationPage']

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


class ProjectPage(Page):

    # Image
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='The image that is displayed' +
                  'on a projecttile in a project list'
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

    organisation = models.ForeignKey(
        'projects.OrganisationPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    # Title
    title_en = models.CharField(max_length=255, blank=True)
    title_de = models.CharField(max_length=255, blank=True)
    title_it = models.CharField(max_length=255, blank=True)
    title_fr = models.CharField(max_length=255, blank=True)
    title_sv = models.CharField(max_length=255, blank=True)
    title_sl = models.CharField(max_length=255, blank=True)
    title_da = models.CharField(max_length=255, blank=True)

    # teaser
    teaser_en = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_de = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_it = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_fr = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_sv = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_sl = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")
    teaser_da = models.TextField(
        max_length=400, blank=True, help_text="Max. 400 Characters")

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

    subpage_types = [
        'projects.AdhocracyProjectPage', 'projects.FlashpollProjectPage']

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
    widget = models.CharField(max_length=255)
    initial_url = models.CharField(max_length=255)
    locale = models.CharField(max_length=2, blank=True,
                              help_text=("Leave blank to use the language "
                                         "that is set in the CMS"))

    adhocracy_panel = [
        FieldPanel('widget'),
        FieldPanel('initial_url'),
        FieldPanel('locale')
    ]

    general_panels = [
        FieldPanel('title', classname='title'),
        FieldPanel('slug'),
        ImageChooserPanel('image'),
        FieldPanel('projecttype'),
        FieldPanel('organisation')
    ]

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('title_en'),
                FieldPanel('teaser_en'),
            ],
            heading="English",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_de'),
                FieldPanel('teaser_de')
            ],
            heading="German",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_it'),
                FieldPanel('teaser_it')
            ],
            heading="Italien",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_fr'),
                FieldPanel('teaser_fr')
            ],
            heading="French",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sv'),
                FieldPanel('teaser_sv')
            ],
            heading="Swedish",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_sl'),
                FieldPanel('teaser_sl')
            ],
            heading="Slovene",
            classname="collapsible"
        ),
        MultiFieldPanel(
            [
                FieldPanel('title_da'),
                FieldPanel('teaser_da')
            ],
            heading="Danish",
            classname="collapsible"
        )

    ]

    edit_handler = TabbedInterface([
        ObjectList(general_panels, heading='General'),
        ObjectList(content_panels, heading='Content'),
        ObjectList(adhocracy_panel, heading='Adhocracy')

    ])


class FlashpollProjectPage(ProjectPage):

    embedurl = models.URLField()

    flashpoll_panel = [
        FieldPanel('embedurl')
    ]

    general_panels = [
        FieldPanel('title', classname='title'),
        FieldPanel('slug'),
        ImageChooserPanel('image'),
        FieldPanel('projecttype'),
        FieldPanel('organisation')
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
        ObjectList(flashpoll_panel, heading='Flashpoll')
    ])


class Project(models.Model):
    project = models.ForeignKey(
        ProjectPage)

    panels = [
        FieldPanel('project')
    ]

    class Meta:
        abstract = True


class ProjectOrganisations(Orderable, Project):
    page = ParentalKey(
        'projects.OrganisationPage',
        related_name='organisation_projects',
        null=True, blank=True)
