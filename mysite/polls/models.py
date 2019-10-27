from django.db import models
from django.utils import timezone

class Userlogin(models.Model):

    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 50)
    image = models.ImageField(default = 'user.png')

    def __str__(self):
        return '<Image:{}'.format(self.image)

class Status(models.Model):
    name = models.CharField(max_length = 50, default = "")
    email = models.CharField(max_length = 30)
    status = models.TextField(max_length = 100000000)
    like = models.BigIntegerField(default = 0)
    time = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return '< Email:{}, Status:{}>'.format(self.email, self.status)

