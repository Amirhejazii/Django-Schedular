from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from .tasks import sendings_mail

@receiver(post_save, sender=Task)
def sending_mail(sender, instance, created, **kwargs):
    if created:
        sendings_mail.delay(task_id=instance.id)
    
