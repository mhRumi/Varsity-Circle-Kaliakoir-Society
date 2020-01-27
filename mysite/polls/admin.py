from django.contrib import admin
from .models import Status, Profile, Education, Work, Comments, StatusLike

admin.site.register(Status)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Comments)
admin.site.register(StatusLike)
# Register your models here.
