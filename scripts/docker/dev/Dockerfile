FROM python:3.10-slim

ARG DJANGO_PORT=9000

EXPOSE $DJANGO_PORT

ENV BACKEND_REDIS_HOST redis
ENV BACKEND_REDIS_PORT 6379
ENV BACKEND_ADMINS newadmin:Aa12345,newadmin2:Aa12345

ENV BACKEND_DB_HOST pg_db
ENV BACKEND_DB_PORT 5432

ENV DJANGO_PORT $DJANGO_PORT
ENV DJANGO_SETTINGS_MODULE core.settings.development

ENV \
    #python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    #poetry
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VERSION=1.2.2

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get install netcat -y \
    && apt-get install build-essential python3.9-dev -y \
    && python -m pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.in-project true

RUN mkdir -p /sms-gateway \
             /etc/sms-gateway/backend

WORKDIR /sms-gateway
COPY poetry.lock pyproject.toml /sms-gateway/
RUN poetry install --no-dev

COPY scripts/docker/dev/entrypoint.sh /sms-gateway/entrypoint
RUN chmod +x /sms-gateway/entrypoint
ENTRYPOINT ["/sms-gateway/entrypoint"]

COPY backend /sms-gateway/backend