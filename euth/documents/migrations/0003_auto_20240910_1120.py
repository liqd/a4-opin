# Generated by Django 3.2.20 on 2024-09-10 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('euth_documents', '0002_add_paragraph_ordering_by_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paragraph',
            name='document',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Paragraph',
        ),
    ]
