#!/bin/bash

cd /app/
celery -A wapico.celery flower --port=5566 --url-prefix=flower --inspect-options=footer_template:templates/flower_header.html