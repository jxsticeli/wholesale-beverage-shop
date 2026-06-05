#!/usr/bin/env bash

pip install -r requirements.txt

cd beverage_shop

python manage.py collectstatic --noinput

python manage.py migrate