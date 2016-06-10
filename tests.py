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
