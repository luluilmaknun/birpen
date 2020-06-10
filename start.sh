#!/bin/bash
echo "Starting birpen ..."
env/bin/pip3 install -r requirements.txt
yarn install
yarn build
env/bin/python3 manage.py migrate
sudo env/bin/python3 manage.py runserver 0:80 >out 2>&1 &
