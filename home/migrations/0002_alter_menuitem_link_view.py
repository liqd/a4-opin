# Generated by Django 3.2.20 on 2024-10-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='link_view',
            field=models.CharField(blank=True, choices=[], max_length=100),
        ),
    ]
