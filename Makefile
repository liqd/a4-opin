all: install fixtures

install:
	npm install
	npm run build
	if [ ! -f bin/python3 ]; then python3 -m venv .; fi
	bin/python3 -m pip install -r requirements.txt
	bin/python3 manage.py migrate
	bin/python3 manage.py loaddata site-dev

fixtures:
	bin/python3 manage.py loaddata site-dev
	bin/python3 manage.py loadtestdata user_management.User:20
	bin/python3 manage.py loadtestdata euth_organisations.Organisation:5
	bin/python3 manage.py loadtestdata euth_projects.Project:2

watch:
	trap 'kill %1'; \
	npm run watch & \
	bin/python3 manage.py runserver 8000

server:
	bin/python3 manage.py runserver 8000
