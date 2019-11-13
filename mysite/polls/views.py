from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Status, Userlogin, Education, Work, Profile
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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
@login_required
def timeline(request):
    status = Status.objects.order_by('-id') 
    user = Userlogin.objects.filter(name = 'Rumi')
    image = ""
    for s in user:
        image = s.image
    print(image)
    return render(request, 'timeline.html', {'status': status}, {'image': image})

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
        status = Status.objects.order_by('-id')
        return render(request, 'timeline.html', {'status': status})
    else:
        return redirect('/')

def galary(request):
    image = Profile.objects.all()
    for i in image:
        print(i.image)
    return render(request, 'galary.html', {'image': image})

@login_required
def me(request):
    work = Work.objects.all()
    print("*******************************************") 
    print(User.username) 
    print("*******************************************")    
    info = Education.objects.filter( user_id = User.id)

    return render(request, 'me.html', { 'work': work, 'education': info} )

def logoutUser(request):
    logout(request)
    return redirect('/')
