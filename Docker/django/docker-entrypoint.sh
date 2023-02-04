#!/bin/bash

#python manage.py initadmin
######################################
#### planning to write initadmin  ####
######################################

apt-get update

mkdir -p /app/wapico/static
cd /app
pip3 install poetry
poetry config virtualenvs.create false
poetry install
# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput
python manage.py loaddata data.json
#collect static
python manage.py collectstatic --noinput