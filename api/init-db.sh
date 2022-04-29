#!/usr/bin/bash

rm -rf ./crm/migrations
rm -rf db.sqlite3

python manage.py makemigrations crm

python manage.py migrate

python manage.py loaddata fixture-rank.json
python manage.py loaddata fixture-seats.json
python manage.py loaddata fixture-tax.json
python manage.py create_admin
python manage.py runserver 0.0.0.0:8000
