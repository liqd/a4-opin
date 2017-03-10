from django.core.management.commands import makemessages
import adhocracy4
import euth


class Command(makemessages.Command):

    def find_files(self, root):
        a4_path = adhocracy4.__path__[0]
        euth_path = euth.__path__[0]
        return super().find_files(a4_path) + super().find_files(euth_path)
