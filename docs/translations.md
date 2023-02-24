# Translations

## Languages

  - source code uses en_GB (arguments to gettext == msg_id )
     - lower case (except for first word of title or sentence)
  - support many languages with transifex (en, de, it, fr,
    sv, sl, da, el, ka, mk, bg as of 03/2022)

## Workflow

### Install the transifex client if you haven't already
- see https://github.com/transifex/cli for instructions

### Adding new strings to translate and get new translations from transifex

Please follow the [docs from a+](https://github.com/liqd/adhocracy-plus/blob/main/docs/languages_and_translations.md).


### Adding a new language

  - add language to LANGUAGES in euth_wagtail/settings/base.py
  - make migrations - this will add new language to wagtail fields

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
