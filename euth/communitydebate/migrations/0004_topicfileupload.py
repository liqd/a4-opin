# Generated by Django 2.2.12 on 2020-04-29 09:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import euth.offlinephases.validators


class Migration(migrations.Migration):

    dependencies = [
        ('euth_communitydebate', '0003_topic_add_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicFileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=256)),
                ('document', models.FileField(upload_to='communitydebate/documents', validators=[euth.offlinephases.validators.validate_file_type_and_size])),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='euth_communitydebate.Topic')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
