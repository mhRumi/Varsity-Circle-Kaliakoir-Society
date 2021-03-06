from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Status, Education, Work, Profile, Comments, StatusLike
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
name = ""

# Create your views here.
def login(request):

    if(request.method == 'POST'):
        email = request.POST['Email']
        password = request.POST['Password']
        name = email
        user = auth.authenticate(username = email, password = password)
        request.session['userId'] = user.pk
        if(user is not None):
            auth.login(request, user)
            request.session['userId'] = user.pk
            return redirect('/timeline')
        else:
            messages.info(request, 'Incorrect email or password')
            return redirect('/')

    else:
        return render(request, 'Login/login.html')
@login_required
def timeline(request):
    status = Status.objects.order_by('-id') 
    return render(request, 'timeline.html', {'status': status})

def registration(request):
    if( request.method == 'POST'):
        Fname = request.POST['FName']
        Lname = request.POST['LName']
        email = request.POST['Email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']

        user = User.objects.create_user(username = email, password = password1, email = email, first_name = Fname, last_name = Lname)
        user.save()
        profile = Profile(image= 'user.png', user_id = user.pk)
        profile.save()
        return render(request, 'Login/login.html')
    else:
        return render(request, 'registration.html')

def status(request):
    if(request.method == 'POST'):
        status = request.POST['status']
        user = User.objects.get(pk = request.session.get('userId'))
        new_status = Status(email = user.email, status = status, like = 0, name = user.first_name)
        new_status.save()
        status = Status.objects.order_by('-id')
        return render(request, 'timeline.html', {'status': status})
    else:
        return redirect('/')

def galary(request):
    image = Profile.objects.all()
    return render(request, 'galary.html', {'image': image})

@login_required
def me(request):
    work = Work.objects.filter(user_id = request.session.get('userId'))   
    info = Education.objects.filter(user_id = request.session.get('userId'))
    return render(request, 'me.html', { 'work': work, 'education': info} )

def logoutUser(request):
    logout(request)
    return redirect('/')

def members(request):
    return render(request, 'members.html')

def deletePost(request, pk):
    if(request.method == 'POST'):
        model = Status.objects.get(pk=pk)
        model.delete()
    return redirect('/timeline')

def comments(request):
    if(request.method == 'POST'):
        name = request.POST['Name']
        cmnt = request.POST['Comment']
        pk = request.POST['PK']
        request.session['PostId'] = pk
        New_comment = Comments(Name = name, comment = cmnt, user_id = pk)
        New_comment.save()
    return redirect('/viewStatus')

def deleteComment(request):
    if(request.method == 'POST'):
        pk = request.POST['pk']
        comment = Comments.objects.get(pk = pk)
        comment.delete()
    return redirect('/viewStatus')

def viewStatus(request):
    if(request.method == 'POST'):
        pk = request.POST['pk']
        request.session['PostId'] = pk
        status = Status.objects.get(pk = pk)
        comment = Comments.objects.filter(user_id = pk) 
        return render(request, 'ViewStatus.html', {'status': status, 'comment': comment, 'postId': pk})
    else:
        postId = request.session.get('PostId')
        status = Status.objects.get(pk = postId)
        comment = Comments.objects.filter(user_id = postId) 
        return render(request, 'ViewStatus.html', {'status': status, 'comment': comment, 'postId': postId})

def like(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        statusId = request.POST['statusId']
        alreadyLiked = StatusLike.objects.filter(email = email, model_id = statusId)
        if(alreadyLiked.count() == 0):
            new_data = StatusLike(email = email, model_id = statusId)
            new_data.save()
        return redirect('/timeline')
        
