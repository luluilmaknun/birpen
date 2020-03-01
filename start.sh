#!/bin/bash
echo "Starting birpen ..."
env/bin/python3 manage.py makemigrations
env/bin/python3 manage.py migrate
sudo env/bin/python3 manage.py runserver 0:80 >out 2>&1 &
