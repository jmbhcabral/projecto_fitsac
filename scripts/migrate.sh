#!/bin/sh
echo 'Executando Migrate.sh'
makemigrations.sh
python manage.py migrate --noinput