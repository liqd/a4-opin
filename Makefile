all: install fixtures

VIRTUAL_ENV ?= bin
SOURCE_DIRS = euth euth_wagtail home search projects

install:
	npm install
	npm run build
	if [ ! -f $(VIRTUAL_ENV)/python3 ]; then python3 -m venv .; fi
	$(VIRTUAL_ENV)/python3 -m pip install -r requirements.txt
	$(VIRTUAL_ENV)/python3 manage.py migrate
	$(VIRTUAL_ENV)/python3 manage.py loaddata site-dev

fixtures:
	$(VIRTUAL_ENV)/python3 manage.py loaddata site-dev
	$(VIRTUAL_ENV)/python3 manage.py loadtestdata user_management.User:20
	$(VIRTUAL_ENV)/python3 manage.py loadtestdata euth_organisations.Organisation:5
	$(VIRTUAL_ENV)/python3 manage.py loadtestdata euth_projects.Project:2

watch:
	trap 'kill %1' SIGINIT; \
	npm run watch & \
	$(VIRTUAL_ENV)/python3 manage.py runserver 8000

server:
	$(VIRTUAL_ENV)/python3 manage.py runserver 8000

test:
	$(VIRTUAL_ENV)/py.test

lint:
	$(VIRTUAL_ENV)/isort -rc -c $(SOURCE_DIRS)
	$(VIRTUAL_ENV)/flake8 $(SOURCE_DIRS) --exclude migrations,settings
	npm run lint
