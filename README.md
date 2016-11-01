# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.9.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)

##Fuencioneeeeeeeeeee

## Estado de la integracion
[ ![Codeship Status for rf-blanco1140/pruebaCodeshipCodaci](https://app.codeship.com/projects/04d52290-8283-0134-ada8-36079b336971/status?branch=master)](https://app.codeship.com/projects/182518)

##Estado del codigo
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fd51a0652b994fe58424212c133a0883)](https://www.codacy.com/app/blancos2004/pruebaCodeshipCodaci?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rf-blanco1140/pruebaCodeshipCodaci&amp;utm_campaign=Badge_Grade)