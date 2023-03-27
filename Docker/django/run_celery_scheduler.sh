#!/bin/bash

cd /app/
celery -A wapico.celery beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
