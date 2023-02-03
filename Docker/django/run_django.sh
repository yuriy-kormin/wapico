#!/bin/bash

#python manage.py initadmin
######################################
#### planning to write initadmin  ####
######################################

apt-get update

pip3 install poetry
poetry config virtualenvs.create false
poetry install

# Apply database migrations
echo "Apply database migrations"
python /app/manage.py migrate --noinput

#collect static
python /app/manage.py collectstatic --noinput