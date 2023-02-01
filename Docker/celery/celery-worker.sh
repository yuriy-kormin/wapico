#!/bin/bash


# Start server
echo "Starting celery worker"
celery -A wapico.celery worker -l info