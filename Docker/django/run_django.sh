#!/bin/bash


cd /app

#run gunicorn
gunicorn wapico.wsgi:application --bind 0.0.0.0:8000
