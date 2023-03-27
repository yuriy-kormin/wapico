MANAGE := poetry run python3 manage.py

start:
	${MANAGE} runserver 127.0.0.1:8000
shell:
	${MANAGE} shell_plus --plain
migrate:
	${MANAGE} makemigrations
	${MANAGE} migrate
collectstatic:
	poetry run python manage.py collectstatic --no-input --clear
test:
	${MANAGE} test
install:
	poetry install
lint:
	poetry run flake8 wapico --exclude migrations
celery:
	celery -A wapico.celery worker -l INFO --concurrency=500 --pool=eventlet
scheduler:
	celery -A wapico.celery beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
flower:
	celery -A wapico.celery flower --port=81
mock:
	poetry run python wapico/mock_server.py
