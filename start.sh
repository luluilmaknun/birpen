#!/bin/bash
echo "Starting birpen ..."
sudo env/bin/python3 manage.py runserver 0:80 >out 2>&1 &
