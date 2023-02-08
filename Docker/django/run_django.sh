#!/bin/bash


cd /app

#run gunicorn
python manage.py migrate --noinput
gunicorn wapico.wsgi:application --bind 0.0.0.0:8000
