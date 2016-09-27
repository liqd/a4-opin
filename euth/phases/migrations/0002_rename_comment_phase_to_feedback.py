from django.db import migrations, models


def rename_comment_to_feedback(apps, schema_editor):
    Phase = apps.get_model('euth_phases', 'Phase')
    Phase.objects.filter(type='euth_ideas:040:comment')\
                 .update(type='euth_ideas:040:feedback')


def rename_feedback_to_comment(apps, schema_editor):
    Phase = apps.get_model('euth_phases', 'Phase')
    Phase.objects.filter(type='euth_ideas:040:feedback')\
                 .update(type='euth_ideas:040:comment')


class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('euth_phases', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            rename_comment_to_feedback,
            rename_feedback_to_comment
        ),
    ]
