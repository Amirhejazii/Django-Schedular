from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    time_to_send = models.DateTimeField()
    precondition_tasks = models.ManyToManyField('self', blank=True)
    
    def __str__(self):
        return self.title
    