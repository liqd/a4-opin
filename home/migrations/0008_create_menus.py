# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def create_menus(apps, schema_editor):

    NavigationMenu = apps.get_model('home.NavigationMenu')

    # Create Footer Navigation
    NavigationMenu.objects.create(
        menu_name="footer"
    )

    # Create TopMenu Navigation
    NavigationMenu.objects.create(
        menu_name="topmenu"
    )


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20160205_1508'),
    ]

    operations = [
        migrations.RunPython(create_menus),
    ]
