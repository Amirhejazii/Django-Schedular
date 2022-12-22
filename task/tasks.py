#from celery.decorators import task
from schedular.celery import app
from celery.utils.log import get_task_logger
import datetime
from django.core.mail import send_mail
from schedular.settings import EMAIL_HOST_USER
from .models import Task
from django.utils import timezone


logger = get_task_logger(__name__)
app.config_from_object('django.conf:settings')
@app.task(name='send mail')
def sendings_mail(task_id):
    
    task = Task.objects.get(id=task_id)
    email = task.owner.email
    time_to_send = task.time_to_send
    title = task.title
    description = task.description
    
    if task.precondition_tasks.all().exists():
        precondition_tasks = task.precondition_tasks.all()
        if precondition_tasks.count() == 1:
            pre_task = precondition_tasks.first()
            while timezone.now() < pre_task.time_to_send:
                continue
            else:
                send_mail(subject=pre_task.title,message=pre_task.description,from_email=EMAIL_HOST_USER,recipient_list=pre_task.owner.email,fail_silently=False)
                
        elif precondition_tasks.count() >1:
            for pre_task in precondition_tasks:
                while timezone.now() < pre_task.time_to_send:
                    continue
                else:
                    send_mail(subject=pre_task.title,message=pre_task.description,from_email=EMAIL_HOST_USER,recipient_list=pre_task.owner.email,fail_silently=False)

                    
    while timezone.now() < time_to_send:
        continue
    else:
        send_mail(subject=title,message=description,from_email=EMAIL_HOST_USER,recipient_list=[email],fail_silently= False)
        
        