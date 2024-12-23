# Generated by Django 3.2.20 on 2024-09-10 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                "DROP TABLE IF EXISTS background_task",
                "DROP TABLE IF EXISTS background_task_completedtask",
                "DROP TABLE IF EXISTS a4categories_category",
                "DROP TABLE IF EXISTS a4comments_comment",
                "DROP TABLE IF EXISTS a4maps_areasettings",
                "DROP TABLE IF EXISTS a4phases_phase",
                "DROP TABLE IF EXISTS a4polls_answer",
                "DROP TABLE IF EXISTS a4polls_othervote",
                "DROP TABLE IF EXISTS a4polls_vote",
                "DROP TABLE IF EXISTS a4polls_choice",
                "DROP TABLE IF EXISTS a4polls_question",
                "DROP TABLE IF EXISTS a4polls_poll",
                "DROP TABLE IF EXISTS a4modules_item",
                "DROP TABLE IF EXISTS a4modules_module",
                "DROP TABLE IF EXISTS a4projects_project_moderators",
                "DROP TABLE IF EXISTS a4projects_project_participants",
                "DROP TABLE IF EXISTS a4projects_project",
                "DROP TABLE IF EXISTS a4ratings_rating",
                "DROP TABLE IF EXISTS a4reports_report",
                "DROP TABLE IF EXISTS a4administrative_districts_administrativedistrict",
            ],
            reverse_sql=migrations.RunSQL.noop,
        )
    ]
