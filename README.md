
# All the commands run in mac and assumes you have installed all packages. Make sure you install them previously, and use the commands corresponding to your environment (Window / Linux)

## (optional) create python virtual environment
python3 -m venv env

## install django
python -m pip install Django

## activate virtual environment
source env/bin/activate

## deactivate virtual environment
deactivate

## create django project
django-admin startproject myproject

## install mysqlclient engine to connect mysql database
pip install mysqlclient

## generate migration file
python manage.py makemigrations

## generate migration file for new directory (appName)
python manage.py makemigrations appName

## make migration
python manage.py migrate

## install rest framework
pip install djangorestframework

## start the server
python manage.py runserver 

## install all dependency in requirements
pip install -r requirements.txt

