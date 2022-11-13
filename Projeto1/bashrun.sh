#!/bin/bash

python3 manage.py check
python3 manage.py makemigrations app
python3 manage.py sqlmigrate app 0001
python3 manage.py migrate