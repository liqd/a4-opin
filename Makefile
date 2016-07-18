all: help

VIRTUAL_ENV ?= bin
SOURCE_DIRS = euth euth_wagtail home search projects

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
	if [ ! -f $(VIRTUAL_ENV)/python3 ]; then python3 -m venv .; fi
	$(VIRTUAL_ENV)/python3 -m pip install -r requirements/dev.txt
	$(VIRTUAL_ENV)/python3 manage.py migrate
	$(VIRTUAL_ENV)/python3 manage.py loaddata site-dev

fixtures:
	$(VIRTUAL_ENV)/python3 manage.py loaddata site-dev
	$(VIRTUAL_ENV)/python3 manage.py loadtestdata user_management.User:20
	$(VIRTUAL_ENV)/python3 manage.py loadtestdata euth_organisations.Organisation:5
	$(VIRTUAL_ENV)/python3 manage.py loadtestdata euth_projects.Project:2
	$(VIRTUAL_ENV)/python3 manage.py loadtestdata comments.Comment:10

watch:
	trap 'kill %1' SIGINIT; \
	npm run watch & \
	$(VIRTUAL_ENV)/python3 manage.py runserver 8000

server:
	$(VIRTUAL_ENV)/python3 manage.py runserver 8000

test:
	$(VIRTUAL_ENV)/py.test --reuse-db

test-clean:
	$(VIRTUAL_ENV)/py.test --reuse-db --create-db

coverage:
	$(VIRTUAL_ENV)/py.test --reuse-db --cov --cov-report=html

lint:
	EXIT_STATUS=0; \
	$(VIRTUAL_ENV)/isort -rc -c $(SOURCE_DIRS) ||  EXIT_STATUS=$$?; \
	$(VIRTUAL_ENV)/flake8 $(SOURCE_DIRS) --exclude migrations,settings ||  EXIT_STATUS=$$?; \
	npm run lint ||  EXIT_STATUS=$$?; \
	exit $${EXIT_STATUS}
