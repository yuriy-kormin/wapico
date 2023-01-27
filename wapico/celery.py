import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wapico.settings")
app = Celery("wapico")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
