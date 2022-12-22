#!/bin/bash

set -o errexit
set -o nounset

readonly VENV_EXEC=.venv/bin/python3.10

wait_postgres() {
  echo "Waiting for postgres..."
  while ! nc -z $BACKEND_DB_HOST $BACKEND_DB_PORT; do
    sleep 0.1
  done
  echo "PostgreSQL started"
}


run_makemigrations() {
  echo "Running create migration..."
  "${VENV_EXEC}" backend/manage.py makemigrations --noinput
}

run_migrations() {
  echo "Running migrations..."
  "${VENV_EXEC}" backend/manage.py migrate --noinput
}

run_api() {
    "${VENV_EXEC}" backend/manage.py runserver "0.0.0.0:$DJANGO_PORT"
}

wait_postgres
run_makemigrations
run_migrations
run_api