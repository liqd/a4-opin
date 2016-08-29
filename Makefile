all: help

VIRTUAL_ENV ?= .
SOURCE_DIRS = euth euth_wagtail home search projects tests

help:
	@echo OPIN development tools
	@echo
	@echo It will either use a exisiting virtualenv if it was entered
	@echo before or create a new one in the same directory.
	@echo
	@echo usage:
	@echo
	@echo   make install      -- install dev setup
	@echo   make fixtures     -- load example data
	@echo   make watch	  -- development server
	@echo   make test         -- tests on exiting database
	@echo   make test-clean   -- test on new database
	@echo   make lint	  -- lint javascript and python
	@echo   make locales      -- create new po and mo files
	@echo

install:
	npm install
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv .; fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata site-dev

fixtures:
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata site-dev
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata user_management.User:20
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_organisations.Organisation:5
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_organisations.OrganisationTranslation:4
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_projects.Project:20
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata comments.Comment:10
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_modules.Module:10
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_phases.Phase:10
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_ideas.Idea:40

watch:
	trap 'kill %1' SIGINIT; \
	npm run watch & \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8000

server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8000

test:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db

test-clean:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --create-db

coverage:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --cov --cov-report=html

lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/isort -rc -c $(SOURCE_DIRS) ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint ||  EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

locales:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d djangojs
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d django
	$(VIRTUAL_ENV)/bin/python manage.py compilemessages
