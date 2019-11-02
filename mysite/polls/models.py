from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Userlogin(models.Model):

    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 50)
    image = models.ImageField(default = 'user.png', blank = True)

    def __str__(self):
        return '<Image:{}, Name:{} '.format(self.image, self.name)

class Status(models.Model):
    name = models.CharField(max_length = 50, default = "")
    email = models.CharField(max_length = 30)
    status = models.TextField()
    like = models.BigIntegerField(default = 0)
    time = models.DateTimeField(default = timezone.now)

    def __unicode__(self):
        return self.status

    def __str__(self):
        return '< Email:{}, Status:{}>'.format(self.email, self.status)

class UploadPicture(models.Model):
    pass