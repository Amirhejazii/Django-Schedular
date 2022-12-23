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
my roadmap for this project is these fallowing tasks:
1-start project and make two app for project one of them for task and another for user 
2-add models and create migrations for tables
3-customize admin panel 
4-add two groups of users one of them is admin and normal 
5-specify admin panel for two groups to see their own tasks or see all tasks for different groups
6-add readonly field into form of task for normal people beacuse they must to make task for themseleves just
7-customize admin panel for admin group they must access have crud for user and tasks but normal user cant
8-create signals for user beacuse all user must have access to admin panel another signals for tasks to send email when created
9-start celery and redis as message queue and add task.py for sending email
10-send email in wsy of sending emails of precondition tasks then send sub task
11-write api for validating all tasks in db with time to send of perconditions tasks 
12-write test for api
