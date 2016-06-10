from os.path import dirname, join, realpath
from django.test import TestCase


class FormatingTestCase(TestCase):
    def test_yapf(self):
        """
        Check that yapf would do any changes.
        """
        from yapf.yapflib import file_resources
        from yapf import FormatFiles

        files = [realpath(__file__), 'euth']
        recursive = True
        style_config = join(dirname(realpath(__file__)), '.style.yapf')
        files = file_resources.GetCommandLineFiles(files, recursive, [])
        changed = FormatFiles(
            files, None,
            style_config=style_config,
            print_diff=True
        )

        self.assertFalse(changed)

    def test_migrations(self):
        """
        Check if all migrations have been created.
        """
        from django.apps import apps
        from django.conf import settings
        from django.db.migrations.autodetector import MigrationAutodetector
        from django.db.migrations.executor import MigrationExecutor
        from django.db.migrations.state import ProjectState
        from django.db import connections
        from django.db.utils import OperationalError

        changed = set()

        for db in settings.DATABASES.keys():
            try:
                executor = MigrationExecutor(connections[db])
            except OperationalError:
                sys.exit(
                    "Unable to check migrations: cannot connect to database\n"
                )

            autodetector = MigrationAutodetector(
                executor.loader.project_state(),
                ProjectState.from_apps(apps),
            )

            changed.update(
                autodetector.changes(graph=executor.loader.graph).keys()
            )
            self.assertEqual(len(changed), 0)
