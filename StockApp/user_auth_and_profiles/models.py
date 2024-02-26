from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profile")
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save()