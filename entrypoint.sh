#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.3
    done

    echo "PostgreSQL started"
fi



echo "Creating the database tables..."
flask db upgrade

echo "Tables created"


exec "$@"