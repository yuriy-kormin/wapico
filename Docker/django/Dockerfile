FROM python:3.11

#ENV PYTHONUNBUFFERED 1
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV CELERY_DATABASE_RESULT='db+postgresql+psycopg2://wapico:wapico@localhost:5435/wapico'
#ENV DATABASE_URL=postgres://wapico:wapico@pgdatabase:5432/wapico
#ENV DJANGO_SECRET='%ygz@y(^ma*_h_rp92r#srrir+zpiau2i$#740ju$)yyr-dz_n'
#ENV DEBUG=True
#ENV CELERY_BROKER_URL="redis://redis:6379"

RUN mkdir /app/static
COPY . /app/
WORKDIR /app
CMD ["./docker-entrypoint.sh"]
