# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a4projects', '0006_project_typ'),
        ('home', '0028_helppages_example_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helppages',
            name='example_project',
        ),
        migrations.AddField(
            model_name='helppages',
            name='agenda_setting',
            field=models.ForeignKey(related_name='example_project_agenda_setting', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='a4projects.Project', null=True, help_text='Please select an exemplary agenda-setting project.'),
        ),
        migrations.AddField(
            model_name='helppages',
            name='brainstorming',
            field=models.ForeignKey(related_name='example_project_brainstorming', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='a4projects.Project', null=True, help_text='Please select an exemplary brainstorming project.'),
        ),
        migrations.AddField(
            model_name='helppages',
            name='commenting_text',
            field=models.ForeignKey(related_name='example_project_commenting_text', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='a4projects.Project', null=True, help_text='Please select an exemplary commenting-text project.'),
        ),
        migrations.AddField(
            model_name='helppages',
            name='flashpoll',
            field=models.ForeignKey(related_name='example_project_flashpoll', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='a4projects.Project', null=True, help_text='Please select an exemplary flashpoll project.'),
        ),
        migrations.AddField(
            model_name='helppages',
            name='idea_challenge',
            field=models.ForeignKey(related_name='example_project_idea_challenge', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='a4projects.Project', null=True, help_text='Please select an exemplary idea-challenge project.'),
        ),
        migrations.AddField(
            model_name='helppages',
            name='map_brainstorming',
            field=models.ForeignKey(related_name='example_project_map_brainstorming', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='a4projects.Project', null=True, help_text='Please select an exemplary map-brainstorming project.'),
        ),
        migrations.AddField(
            model_name='helppages',
            name='map_idea_challenge',
            field=models.ForeignKey(related_name='example_project_map_idea_challenge', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='a4projects.Project', null=True, help_text='Please select an exemplary map-idea-challenge project.'),
        ),
    ]
