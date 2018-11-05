VIRTUAL_ENV ?= venv
SOURCE_DIRS = euth euth_wagtail home tests

.PHONY: all
all: help

.PHONY: help
help:
	@echo OPIN development tools
	@echo
	@echo It will either use a exisiting virtualenv if it was entered
	@echo before or create a new one in the same directory.
	@echo
	@echo usage:
	@echo
	@echo "  make install         -- install dev setup"
	@echo "  make clean           -- delete node modules and venv"
	@echo "  make fixtures        -- load example data"
	@echo "  make server	      -- start a dev server"
	@echo "  make watch           -- start a dev server and rebuild js and css files on changes"
	@echo "  make background      -- start a dev server, rebuild js and css files on changes, and start background processes"
	@echo "  make test            -- tests on exiting database"
	@echo "  make test-lastfailed -- run test that failed last"
	@echo "  make test-clean      -- test on new database"
	@echo "  make coverage        -- write coverage report to dir htmlcov"
	@echo "  make lint            -- lint javascript and python, check for missing migrations"
	@echo "  make po              -- create new po files from the source"
	@echo "  make mo              -- create new mo files from the translated po files"
	@echo "  make tx-mo           -- pull from transifex and create new mo files from the translated po files"
	@echo "  make release         -- build everything required for a release"
	@echo

.PHONY: install
install:
	npm install --no-save
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/bin/python3 ]; then python3 -m venv $(VIRTUAL_ENV); fi
	$(VIRTUAL_ENV)/bin/python3 -m pip install --upgrade -r requirements/dev.txt
	$(VIRTUAL_ENV)/bin/python3 manage.py migrate

.PHONY: clean
clean:
	if [ -d node_modules ]; then rm -r node_modules; fi
	if [ -d venv ]; then rm -r venv; fi

.PHONY: fixtures
fixtures:
	$(VIRTUAL_ENV)/bin/python3 manage.py loaddata site-dev
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_users.User:20
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_organisations.Organisation:5
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_organisations.OrganisationTranslation:4
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata a4projects.Project:10
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata a4modules.Module:15
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata a4phases.Phase:20
	$(VIRTUAL_ENV)/bin/python3 manage.py loadtestdata euth_ideas.Idea:40

.PHONY: server
server:
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8001

.PHONY: watch
watch:
	trap 'kill %1' KILL; \
	npm run watch & \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8001

.PHONY: background
background:
	trap 'kill %1; kill %2' KILL; \
	npm run watch & \
	$(VIRTUAL_ENV)/bin/python3 manage.py process_tasks & \
	$(VIRTUAL_ENV)/bin/python3 manage.py runserver 8001

.PHONY: test
test:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db

.PHONY: test-lastfailed
test-lastfailed:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --last-failed

.PHONY: test-clean
test-clean:
	if [ -f test_db.sqlite3 ]; then rm test_db.sqlite3; fi
	find media -iname 'example_*.jpg' -exec rm {} \+
	$(VIRTUAL_ENV)/bin/py.test

.PHONY: coverage
coverage:
	$(VIRTUAL_ENV)/bin/py.test --reuse-db --cov --cov-report=html

.PHONY: lint
lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/bin/isort -rc -c $(SOURCE_DIRS) --diff ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint --silent ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/bin/python manage.py makemigrations --dry-run --check --noinput || EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}

.PHONY: po
po:
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d djangojs
	$(VIRTUAL_ENV)/bin/python manage.py makemessages -d django
	sed -i 's%#: .*/adhocracy4%#: adhocracy4%' locale/*/LC_MESSAGES/django*.po
	msgen locale/en_GB/LC_MESSAGES/django.po -o locale/en_GB/LC_MESSAGES/django.po
	msgen locale/en_GB/LC_MESSAGES/djangojs.po -o locale/en_GB/LC_MESSAGES/djangojs.po

.PHONY: mo
mo:
	$(VIRTUAL_ENV)/bin/python manage.py compilemessages

.PHONY: tx-mo
tx-mo:
	$(VIRTUAL_ENV)/bin/tx pull -a
	$(VIRTUAL_ENV)/bin/python manage.py compilemessages

.PHONY: release
release: export DJANGO_SETTINGS_MODULE ?= euth_wagtail.settings.build
release:
	npm install --silent
	npm run build
	$(VIRTUAL_ENV)/bin/python3 -m pip install -r requirements.txt -q
	$(VIRTUAL_ENV)/bin/python3 manage.py compilemessages -v0
	$(VIRTUAL_ENV)/bin/python3 manage.py collectstatic --noinput -v0
