# CMS for EUTH Project

![Build Status](https://github.com/liqd/a4-opin/actions/workflows/django.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/liqd/a4-opin/badge.svg?branch=main)](https://coveralls.io/github/liqd/a4-opin?branch=main)

# WARNING
Since commit da29d7fabdeaa1594d5fdd0fe24eceab143e004d this project is being
refactored towards a wagtail only project to be used as an informational
website, all participation parts are being removed.

**DO NOT UPGRADE to the main branch or any version beyond v2401 or
otherwise you will lose data**.

## Requires

 * nodejs (+ npm)
 * python 3.x (+ virtualenv + pip)
 * libmagic
 * libjpeg
 * libpq (only if postgres should be used)

## Setup and development

Use the provided Makefile to start development. It comes with a help command
`make help` . The initials steps to get the software running should be:

```
git clone https://github.com/liqd/a4-opin.git  # clone repository
cd a4-opin # change to cloned repo
make install
make fixtures
make watch
```

## django-allauth setup

Visit the Django Admin and follow these steps:

1. Add a `Site` for your domain, matching `settings.SITE_ID`.
2. For each OAuth based provider, add a *Social application* (part of the *Social accounts* app).
3. Fill in the site and the OAuth app credentials obtained from the provider.

See [django-allauth providers documentation](https://django-allauth.readthedocs.io/en/latest/providers.html)
for more information on how to configure every provider.

There are no OAuth based providers activated for development. You have to add
them manually to `INSTALLED_APPS` to use them locally.

GitHub example:

```python
INSTALLED_APPS = [
    # Other apps
    'allauth.socialaccount.providers.github',
]
```
