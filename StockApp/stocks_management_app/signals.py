from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import Models

@receiver(post_save, sender=Models)
def my_model_post_save(sender, instance, **kwargs):
    # Signal handling code here
    pass