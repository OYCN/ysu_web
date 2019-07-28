#!/usr/bin/env bash
#sed -i 's/\r$//' filename

python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py loaddata model_init.json

#python ./manage.py createsuperuser

#python ./manage.py collectstatic

