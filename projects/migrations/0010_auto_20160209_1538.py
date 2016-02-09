# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('projects', '0009_auto_20160208_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationsPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, to='wagtailcore.Page', parent_link=True, primary_key=True, auto_created=True)),
                ('title_en', models.CharField(max_length=255, blank=True)),
                ('title_de', models.CharField(max_length=255, blank=True)),
                ('title_it', models.CharField(max_length=255, blank=True)),
                ('title_fr', models.CharField(max_length=255, blank=True)),
                ('title_sv', models.CharField(max_length=255, blank=True)),
                ('title_sl', models.CharField(max_length=255, blank=True)),
                ('title_da', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProjectOrganisations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='country',
            field=django_countries.fields.CountryField(help_text='Where is theOrganisation located', max_length=2, default='DE'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='description_da',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='description_de',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='description_en',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='description_fr',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='description_it',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='description_sl',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='description_sv',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True, related_name='+', help_text='The image that is displayedon a organisationtile in an organisation list'),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='name_da',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='name_de',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='name_en',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='name_fr',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='name_it',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='name_sl',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='name_sv',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='teaser_da',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='teaser_de',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='teaser_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='teaser_fr',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='teaser_it',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='teaser_sl',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='organisationpage',
            name='teaser_sv',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='projectpage',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='projects.OrganisationPage', null=True, related_name='+'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True, related_name='+', help_text='The image that is displayedon a projecttile in a project list'),
        ),
        migrations.AddField(
            model_name='projectorganisations',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='organisation_projects', to='projects.OrganisationPage'),
        ),
        migrations.AddField(
            model_name='projectorganisations',
            name='project',
            field=models.ForeignKey(to='projects.ProjectPage'),
        ),
    ]
