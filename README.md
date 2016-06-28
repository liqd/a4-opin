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
bin/python manage.py migrate
bin/python manage.py createsuperuser
bin/python manage.py runserver
```
Service should now be running on [localhost:8000](http://localhost:8000/admin)

## Tests

Unitest are working with py.test.

 * run `py.test`
 * with coverage html `py.test --cov --cov-report=html`
