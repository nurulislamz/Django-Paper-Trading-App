from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import Stock

@receiver(post_save, sender=Stock)
def my_model_post_save(sender, instance, **kwargs):
    # Signal handling code here
    pass