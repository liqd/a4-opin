# String translation with Transifex

Opin uses Transifex to translate strings using *.po and *.mo files.

## Pulling translations from Transifex

To update the translations in *.po files, you have to pull the latest
versions using the [`bin/tx pull -a`](http://docs.transifex.com/client/pull/) command.
If this does not work, add a `-f` to the command to force the pulling.

## Extracting Strings

Since translatable strings are located both in Python code as well as in
JavaScript it is necessary to extract strings from both domains. This is
done using [`bin/python manage.py makemessages -a`](https://docs.djangoproject.com/es/1.10/ref/django-admin/#makemessages). The following
commands update/create *.po file with the new strings found.
#### for *.py, *.html and *.txt

```
bin/python manage.py makemessages -a
```

#### for *.js

```
bin/python manage.py makemessages -a -d djangojs
```

## Pushing new strings to Transifex

To push the newly extracted strings to Transifex, you have to push the
changes with [`bin/tx push -t`](http://docs.transifex.com/client/push/). To push the source files (*.po files
of the project's source language - English) as well, run `bin/tx push -s -t`.
When pushing source files, be careful not to [override files in Transifex](http://docs.transifex.com/client/push/#how-source-string-updates-are-handled).

## Compiling

After pulling translations from Transifex you might want to compile the
*.po files into *.mo files. This again is done with the manage.py, run:
[`bin/python manage.py compilemessages`](https://docs.djangoproject.com/es/1.10/ref/django-admin/#django-admin-compilemessages).
