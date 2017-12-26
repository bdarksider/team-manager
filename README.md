# Team Manager APIs

CURD operation for managing team memebers.

## Installation

Install mysql database connector

sudo apt-get install python3-dev

sudo apt-get install python3-dev libmysqlclient-dev

sudo apt-get install mysql-server

git clone https://github.com/bdarksider/team-manager.git

cd team-manager

pip install requirements.txt

edit mysql.cnf for db connections

open mysql cli

CREATE DATABASE DATABASE_NAME CHARACTER SET utf8;

to launch server:
python manage.py runserver


## Tests
python manage.py test

## Postman
FOR POSTMAN TESTING IMPORT postman-api.json

## Docs
http://localhost:8000/docs

## APIs

1. Get Team METHOD: GET url: http://localhost:8000/team/
curl -X GET \
  http://localhost:8000/team/ \
  -H 'accept: application/json' \
  -H 'cache-control: no-cache' \

2. Add Team Member METHOD: POST url: http://localhost:8000/team/
curl -X POST \
  http://localhost:8000/team/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "role": "1",
    "first_name": "bejoy",
    "last_name": "george",
    "phone_number": "+919090909090",
    "email": "a@a.com"
}'

    Note: role 1 for Admin, 0 for regular

3. Edit Team Member METHOD: PUT/PATCH url: http://localhost:8000/team/<user-id>/
curl -X PUT \
  http://localhost:8000/team/1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "role": "1",
    "first_name": "efw",
    "last_name": "efw",
    "phone_number": "+3838383838",
    "email": "a@a.com"
}'

4. Delete Team Member METHOD: DELETE url: http://localhost:8000/team/<user-id>/
curl -X DELETE \
  http://localhost:8000/team/1/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
    "role": "1",
    "first_name": "efw",
    "last_name": "efw",
    "phone_number": "+3838383838",
    "email": "a@a.com"
}'

