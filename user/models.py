from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.db.models.signals import pre_save

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

