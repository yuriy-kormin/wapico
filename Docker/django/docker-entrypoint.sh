#!/bin/bash

#python manage.py initadmin
######################################
#### planning to write initadmin  ####
######################################

#apt-get update

mkdir -p /app/wapico/static
cd /app
pip3 install poetry
poetry config virtualenvs.create false
poetry install
# Apply database migrations
#collect static
python manage.py collectstatic --noinput
echo "createsuperuser"
python manage.py createsuperuser --noinput \
      --username $DJANGO_SUPERUSER_USERNAME \
      --email $DJANGO_SUPERUSER_EMAIL
