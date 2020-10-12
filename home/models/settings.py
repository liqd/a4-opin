from django.db import models
from wagtail.admin import edit_handlers
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.models import register_setting

from euth.blueprints.names import BlueprintNames


class BlueprintSettingsMeta(models.base.ModelBase):
    """
    Metaclass for adding a project foreign keys for each blueprint.
    """

    def __new__(cls, name, bases, namespace):
        panels = namespace['panels']
        blueprint_names = namespace['blueprint_names']

        for member in blueprint_names:
            namespace[member.name] = models.ForeignKey(
                'a4projects.Project',
                on_delete=models.SET_NULL,
                null=True,
                blank=True,
                related_name='example_project_{}'.format(member.name),
                help_text='Please select an exemplary {} project.'.format(
                    member.value
                ),
            )
            panels += [edit_handlers.FieldPanel(member.name)]
        return super().__new__(cls, name, bases, namespace)


@register_setting
class HelpPages(BaseSetting, metaclass=BlueprintSettingsMeta):
    guidelines_page = models.ForeignKey(
        'wagtailcore.Page',
        on_delete=models.SET_NULL,
        null=True,
        help_text="Please add a link to the guideline page."
    )

    panels = [
        edit_handlers.PageChooserPanel('guidelines_page'),
    ]

    blueprint_names = BlueprintNames
