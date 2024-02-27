from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(default = 0.00, 
                                  decimal_places = 2,
                                  max_digits = 10)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save()