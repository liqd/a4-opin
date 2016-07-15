# CMS for EUTH Project

## Requires

 * nodejs (+ npm)
 * python 3.x (+ virtualenv + pip)


## How to start

Install the application and its dependencies.

```
git clone https://github.com/liqd/euth_wagtail.git  # clone repository
cd euth_wagtail
npm install                                         # install webpack
npm run build                                       # run webpack
python3 -m venv .                                   # setup virualenv
bin/python3 -m pip install -r requirements.txt      # install requirements
bin/python3 manage.py migrate
bin/python3 manage.py loaddata site-dev
bin/python3 manage.py createsuperuser
bin/python3 manage.py runserver
```
Service should now be running on [localhost:8000](http://localhost:8000/admin)

## Tests

Unitest are working with py.test.

 * run `py.test`
 * with coverage html `py.test --cov --cov-report=html`

## Development

 * for python and css/scss just use `bin/python manage.py runserver`
 * for js / react keep webpack running `npm run watch`

## Locales

The project relies on the django i18n framework (also for the transaltions in js)

```
bin/python manage.py makemessages -d djangojs
bin/python manage.py makemessages -d django
bin/python manage.py compilemessages
```


## Testdata

You can use autofixtures to create some data, e.g. run:

 * to create Users:
```
python manage.py loadtestdata user_management.User:<number of users you want to create>
```
* to create Organisations:
```
python manage.py loadtestdata euth_organisations.Organisation:<number of organisations you want to create>
```
* to create Projects:
```
python manage.py loadtestdata euth_projects.Project:<number of projects you want to create>
```
* to create Comments on the homepage:
```
python manage.py loadtestdata comments.Comment:<number of comments you want to create>
```
