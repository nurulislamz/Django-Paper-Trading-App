from django.db import models
import datetime as dt

# Create your models here.
class APICount(models.Model):
    count = models.IntegerField(default=0)
    date = models.DateTimeField(default=dt.datetime.now())

    def save(self, *args, **kwargs):
        if not self.pk and APICount.objects.exists():
            return
        return super(APICount, self).save(*args, **kwargs)  