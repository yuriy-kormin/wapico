#!/bin/bash

#python manage.py initadmin
######################################
#### planning to write initadmin  ####
######################################

apt-get update

pip3 install poetry
poetry config virtualenvs.create false
poetry install

celery -A wapico.celery worker -l info