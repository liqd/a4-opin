all: help

VIRTUAL_ENV ?= venv
SOURCE_DIRS = euth euth_wagtail home tests

help:
	@echo OPIN development tools
	@echo
	@echo It will either use a exisiting virtualenv if it was entered
	@echo before or create a new one in the same directory.
	@echo
	@echo usage:
	@echo
	@echo "  make install      -- install dev setup"
	@echo "  make fixtures     -- load example data"
	@echo "  make watch	       -- development server"
	@echo "  make test         -- tests on exiting database"
	@echo "  make test-clean   -- test on new database"
	@echo "  make lint	       -- lint javascript and python"
	@echo "  make locales      -- create new po and mo files"
	@echo "  make release      -- build everything required for a release"
	@echo

install:
	npm install
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata site-dev

fixtures:
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata site-dev
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_users.User:20
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_organisations.Organisation:5
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_organisations.OrganisationTranslation:4
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata a4projects.Project:10
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata a4modules.Module:15
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata a4phases.Phase:20
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_ideas.Idea:40

watch:
	trap 'kill %1' KILL; \
	npm run watch & \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8001

server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8001

test:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db

test-lastfailed:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --last-failed

test-clean:
	if [ -f test_db.sqlite3 ]; then rm test_db.sqlite3; fi
	find media -iname 'example_*.jpg' -exec rm {} \+

coverage:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --cov --cov-report=html

lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/isort -rc -c $(SOURCE_DIRS) --diff ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint --silent ||  EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

locales-collect:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d djangojs
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d django
	sed -i 's%#: .*/adhocracy4%#: adhocracy4%' locale/*/LC_MESSAGES/django*.po
	msgen locale/en_GB/LC_MESSAGES/django.po -o locale/en_GB/LC_MESSAGES/django.po
	msgen locale/en_GB/LC_MESSAGES/djangojs.po -o locale/en_GB/LC_MESSAGES/djangojs.po

locales-build:
	$(VIRTUAL_ENV)/bin/tx pull -a
	$(VIRTUAL_ENV)/bin/python manage.py compilemessages

locales:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d djangojs
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d django
	$(VIRTUAL_ENV)/bin/python manage.py compilemessages

.PHONY: release
release:
	npm install --silent
	npm run build
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements.txt -q
	$(VIRTUAL_ENV)/bin/python3 manage.py compilemessages -v0
	$(VIRTUAL_ENV)/bin/python3 manage.py collectstatic --noinput -v0
