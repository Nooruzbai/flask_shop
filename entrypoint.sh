#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$FLASK_DEBUG" = "1" ]
then
  echo "Creating the database tables..."
  flask db init
  flask db migrate
  flask db upgrade

fi

exec "$@"