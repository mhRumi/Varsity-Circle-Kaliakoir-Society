from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Mess(models.Model):
    model = models.ForeignKey(User, on_delete = models.CASCADE)
    message = models.CharField(max_length = 5000)
    seen = models.BooleanField(default = False) 
    time = time = models.DateTimeField(default = timezone.now)
    to = models.BigIntegerField()