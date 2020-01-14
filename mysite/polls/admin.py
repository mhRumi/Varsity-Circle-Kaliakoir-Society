from django.contrib import admin
from .models import Userlogin
from .models import Status, Profile, Education, Work, Comments

admin.site.register(Userlogin)
admin.site.register(Status)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Comments)
# Register your models here.
