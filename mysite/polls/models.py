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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'user.png')
    phone = models.CharField(max_length = 20, null = True, editable = True)
    village = models.CharField(max_length = 50, null = True)
    postOffice = models.CharField(max_length = 50, null = True)
    profession = models.CharField(max_length = 50, null = True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Education(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    varsityName = models.CharField(max_length = 50, null = True)
    joiningDate = models.DateField()
    leavingDate = models.DateField(blank = True, null = True)
    departmentName = models.CharField(max_length = 50, blank = True, null = True)
    description = models.TextField(blank = True)
    degree = models.CharField(max_length = 30, null = True, blank = True )

class Work(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    companyName = models.CharField(max_length = 50, null = True)
    position = models.CharField(max_length = 30, null = True)
    joiningDate = models.DateField()
    leavingDate = models.DateField(blank = True, null = True)
    description = models.TextField(blank = True)

class Comments(models.Model):
    user = models.ForeignKey(Status, on_delete = models.CASCADE)
    Name = models.CharField(max_length = 50, null = True)
    comment = models.CharField(max_length = 2000, null = False)
    time = models.DateTimeField(default = timezone.now)

class StatusLike(models.Model):
    model = models.OneToOneField(Status , on_delete = models.CASCADE)
    email = models.CharField(max_length = 30)

