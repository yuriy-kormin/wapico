FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
COPY wapico/ /app/wapico/
RUN mkdir /app/static/
COPY pyproject.toml /app
COPY README.md manage.py /app/
COPY Docker/django/docker-entrypoint.sh /app/

ENV CELERY_DATABASE_RESULT='db+postgresql+psycopg2://wapico:wapico@localhost:5435/wapico'
ENV DATABASE_URL=postgres://wapico:wapico@pgdatabase:5432/wapico
ENV DJANGO_SECRET='%ygz@y(^ma*_h_rp92r#srrir+zpiau2i$#740ju$)yyr-dz_n'
ENV DEBUG=True
ENV CELERY_BROKER_URL="redis://redis:6379"

WORKDIR /app
RUN apt-get update

# Install GDAL dependencies
#RUN apt-get install -y libgdal-dev g++ --no-install-recommends && \
#    pip install pipenv && \
#    pip install whitenoise && \
#    pip install gunicorn && \
#    apt-get clean -y
#
## Update C env vars so compiler can find gdal
#ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
#ENV C_INCLUDE_PATH=/usr/include/gdal

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["./docker-entrypoint.sh"]
