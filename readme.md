first of all for running project you should do following steps:
```sh
$ git clone https://github.com/gocardless/sample-django-app.git
$ cd sample-django-app
$ git checkout development
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
after that you should make database migrations for tables
```
python3 manage.py migrate
```
now you should start celery with command 

```
celery -A schedular worker -l info
```
then start your redis server

now you can start project
```
python3 manage.py runserver
```
