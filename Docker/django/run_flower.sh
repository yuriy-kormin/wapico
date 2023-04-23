#!/bin/bash

cd /app/
celery -A wapico.celery flower --port=5566 --url-prefix=flower --inspect-options=custom_templates:templates/flower_header.html