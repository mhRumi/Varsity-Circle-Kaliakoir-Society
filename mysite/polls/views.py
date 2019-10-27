from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Status, Userlogin

# Create your views here.
def login(request):

    if(request.method == 'POST'):
        email = request.POST['Email']
        password = request.POST['Password']

        user = auth.authenticate(username = email, password = password)

        if(user is not None):
            auth.login(request, user)
            return timeline(request)
        else:
            messages.info(request, 'Incorrect email or password')
            return redirect('/')

    else:
        return render(request, 'login.html')

def timeline(request):
    status = Status.objects.order_by('time')

    for s in status:
        print(s.email+"  "+ s.status)
        status = Status.objects.order_by('time')
        pic = Userlogin.objects.filter(name = 'admin')
        return render(request, 'timeline.html', {'status': status}, {'pic': pic})

def registration(request):
    if( request.method == 'POST'):
        name = request.POST['Name']
        email = request.POST['Email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']

        if(password1 == password2):

            user = User.objects.create_user(username = name, password = password1, email = email)
            user.save()

            anotherUser = Userlogin(name = name, email = email, password = password1, image= 'user.png')
            anotherUser.save()
            status = Status.objects.order_by('time')
            return render(request, 'timeline.html', {'status': status})
        else:
            messages.info(request, 'Password does not match')
            return redirect('registration')
    else:
        return render(request, 'registration.html')

def status(request):
    if(request.method == 'POST'):
        status = request.POST['status']
        new_status = Status(email = 'rumiswe@gmail.com', status = status, like = 0, name = 'rumi')
        new_status.save()
        status = Status.objects.order_by('time')
        return render(request, 'timeline.html', {'status': status})
    else:
        return redirect('/')
