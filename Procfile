release: python manage.py migrate --noinput; python manage.py loaddata site-heroku
web: gunicorn euth_wagtail.wsgi --log-file -
