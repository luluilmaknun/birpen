#!/bin/bash

PID=$(ps ax | grep manage.py | grep -v grep | head -n1 | awk '{print $1}')

if [[ $PID ]]
then
  ps ax | grep manage.py | grep -v grep | head -n1 | awk '{print $1}' | xargs sudo kill -TERM
fi
