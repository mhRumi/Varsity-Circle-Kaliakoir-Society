from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Message(models.Model):
    model = models.ManyToManyField(User)
    message = models.CharField(max_length = 5000)
    seen = models.BooleanField(default = False) 
    time = time = models.DateTimeField(default = timezone.now)