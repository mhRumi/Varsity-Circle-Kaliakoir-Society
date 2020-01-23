from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
app_name = "message"
def messenger(request):
    data = User.objects.all()
    return render(request, 'Messenger/messenger.html',{'data':data})
