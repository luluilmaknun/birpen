#!/bin/bash

python3 manage.py makemigrations rest_framework_jwt
python3 manage.py migrate
bash seed.sh
gunicorn birpen.wsgi --bind 0.0.0.0:8000