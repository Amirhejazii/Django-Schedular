from .models import User
from django.db.models.signals import pre_save
def access_users_to_admin_panel(sender,instance,*args,**kwargs):
    if not instance.is_staff:
        instance.is_staff = True

pre_save.connect(access_users_to_admin_panel , User)