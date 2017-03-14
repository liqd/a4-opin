from os.path import relpath
from django.core.management.commands import makemessages
import adhocracy4
import euth
import euth_wagtail


class Command(makemessages.Command):
    def find_files(self, root):
        a4_path = super().find_files(adhocracy4.__path__[0])
        euth_path = super().find_files(relpath(euth.__path__[0]))
        euth_wagtail_path = super().find_files(
            relpath(euth_wagtail.__path__[0])
        )
        return a4_path + euth_path + euth_wagtail_path
