# RottenPotatoes

## Welcome!

# Set Up

## Setup the virtual environment

mkvirtualenv rottenpotatoes

## Setup the database

sudo -su postgres psql
CREATE DATABASE databasename;
CREATE USER "username" WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE databasename TO username;
\q
exit

## Install requirements

pip install -r requirements.txt

## Local Settings

Database and other settings should be specified in localsettings.py under RottenPotatoes/

localsettings.py:
DEFAULT_DB = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '',
}