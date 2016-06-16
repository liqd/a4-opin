# CMS for EUTH Project

## Requires

 * nodejs (+ npm)
 * python 3.x (+ virtualenv + pip)


## How to start

1. clone repository
2. `cd euth_wagtail`
3. install bower and sass `npm install bower`
4. create virtualenv (make sure to add virtualenv name to .gitignore)
5. run `pip install -r requirements.txt`
6. run `python manage.py migrate`
7. run `python manage.py createsuperuser`
8. run `python manage.py bower install`
9. run `python manage.py runserver`
10. Browse to  http://localhost:8000/admin

## Tests

 * unit tests usings py.test
     * run `py.test`
