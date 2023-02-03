#!/bin/bash

cd /app/

celery -A wapico.celery worker -l info  --concurrency=500 --pool=eventlet
