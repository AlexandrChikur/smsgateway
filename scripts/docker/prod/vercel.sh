#!/bin/bash

set -o errexit
set -o nounset

readonly VENV_EXEC=python3.10

wait_postgres() {
  echo "Waiting for postgres..."
  while ! nc -z $BACKEND_DB_HOST $BACKEND_DB_PORT; do
    sleep 0.1
  done
  echo "PostgreSQL started"
}

wait_redis() {
  echo "Waiting for redis..."
  while ! nc -z $REDIS_HOST $REDIS_PORT; do
    sleep 0.1
  done
  echo "Redis started"
}

run_install_requirements(){
  echo "Installing requirements..."
  "${VENV_EXEC}" -m pip install -r requirements.txt
}

run_create_admin() {
  echo "Running create default super users..."
  "${VENV_EXEC}" backend/manage.py initadmin
}

run_makemigrations() {
  echo "Running create migration..."
  "${VENV_EXEC}" backend/manage.py makemigrations --noinput
}

run_migrations() {
  echo "Running migrations..."
  "${VENV_EXEC}" backend/manage.py migrate --noinput
}

run_collect_static(){
  echo "Collecting static..."
  "${VENV_EXEC}" backend/manage.py collectstatic --noinput --clear
}

run_api() {
    cd backend
    "../${VENV_EXEC}" -m uvicorn core.asgi:application --host 0.0.0.0 --port $DJANGO_PORT
}

wait_postgres
wait_redis
run_install_requirements
run_makemigrations
run_migrations
run_create_admin
run_collect_static
run_api