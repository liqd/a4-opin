from django.conf.locale import LANG_INFO

# We need to add Maltese to the LANG_INFO,
# because Django does not support Maltese.
# Needs to be changed if Django ever supports Maltese!

LANG_INFO['mt'] = {
                    'bidi': False,
                    'code': 'mt',
                    'name': 'Maltese',
                    'name_local': 'Malti',
                }
