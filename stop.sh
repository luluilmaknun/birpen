#!/bin/bash

PID=$(ps ax | grep manage.py | grep -v grep | head -n1 | awk '{print $1}')
if [[ $PID ]]
then
  echo "Stopping birpen ..."
  ps ax | grep manage.py | grep -v grep | head -n1 | awk '{print $1}' | xargs sudo kill -TERM
else
  echo "Birpen is not running ..."
fi
