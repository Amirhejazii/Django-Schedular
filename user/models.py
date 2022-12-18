from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
USER_PERMISSION_CHOICES=(
    ('A','Admin'),
    ('N','normal')
)

class User(AbstractUser):
    permissions = models.PositiveSmallIntegerField(choices=USER_PERMISSION_CHOICES, null=False)