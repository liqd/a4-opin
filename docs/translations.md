# Translations

## Languages

  - source code uses en_GB (arguments to ugettext == msg_id )
     - lower case (except for first word of title or sentence)
  - support many languages with transifex (en, de, it, fr,
    sv, sl, da, el, ka, mk as of 10/2017)

## Workflow

### Extracting strings from source code

  - required if msg_ids were added or changed
  - pull translated strings from transifex

        tx pull -a

  - run make messages for python/html (domain django)
    and javascript (domain djangojs)

        python manage.py makemessages -d djangojs
        python manage.py makemessages -d django

  - replace absolute paths for a4 strings with relatives

       sed -i 's%#: .*/adhocracy4%#: adhocracy4%' locale/*/LC_MESSAGES/django*.po

  - for en_GB sync msg_ids with msg_strs

        msgen locale/en_GB/LC_MESSAGES/django.po -o locale/en_GB/LC_MESSAGES/django.po
 	      msgen locale/en_GB/LC_MESSAGES/djangojs.po -o locale/en_GB/LC_MESSAGES/djangojs.po

  - after chaining msg_ids, check if translations (except en_GB) need manual merge
  - commit changes
  - always push en_GB to transifex

        tx push -s

  - always push other languages (make sure not to override translated strings)

        tx push -t


### Pulling new translations

  - required if translators worked on transifex
  - update all languages except en_GB

        tx pull -a

  - extract strings afterwards (again) to fix formatting differences

### Compiling local translations

   - required to see translations on local server

         python manage.py compilemessages

   - do not commit those files
   - for dev, stage and prod a build server must do this

### Shortcuts

   - pulling and compiling

         make tx-mo

   - extracting and update for en_GB

         make po

   - compiling

         make mo

### Adding a new language

  - add language to LANGUAGES in euth_wagtail/settings/base.py
  - add 15 fields with the desired language code to home/models.py
    (by searching for an existing language code like '_ka')
  - make migrations

        python manage.py makemigrations home

  - rename migrations
  - add new language to transifex

### Adding a language, that is not supported by Django

  - do everything as described above
  - add a new language field to euth_wagtail/__init__.py
  - pull translations from transifex and compile (described above)


## Caveats

   - project has custom makemessages implementation
      - collects messages from packages `euth`, `euth_wagtail`, `adhcoracy4`
      - disables fuzzy matching on msgmerge
   - en_GB should always equal the msg_ids
      - transifex requires a complete source translation (see [faq](https://docs.transifex.com/faq/all))
      - translators can change *real* strings by overriding en
      - en_GB strings are only used as fallback on the platform
