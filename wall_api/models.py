from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TimeStamp(models.Model):
    '''An abstract base class model that support timestamp functinality'''

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Message(TimeStamp):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

