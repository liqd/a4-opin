# CMS for EUTH Project

## Requires

 * nodejs (+ npm)
 * python 3.x (+ virtualenv + pip)


## How to start

0. npm install -g bower node-sass
1. clone repository
2. cd euth_wagtail
3. create virtualenv (make sure to add virtualenv name to .gitignore)
4. run `pip install -r requirements.txt`
5. run `python manage.py migrate`
6. run `python manage.py createsuperuser`
7. run `python manage.py bower install`
8. run `python manage.py runserver`
9. Browse to  http://localhost:8000/admin
