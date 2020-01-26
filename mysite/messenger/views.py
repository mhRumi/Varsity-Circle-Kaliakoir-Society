from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Mess
from django.db.models import Q
# Create your views here.
app_name = "message"
def messenger(request):
    data = User.objects.all()
    if(request.method == 'GET'):
        toUser = User.objects.filter(pk = request.session.get('to'))
        to = request.session.get('to')
        From = request.session.get('userId')
        msg = Mess.objects.filter(Q(to = to, model_id = From) | Q(to = From, model_id = to))
        return render(request, 'Messenger/messenger.html',{'data':data, 'msg': msg, 'to': to, 'f': From})
    else:
        return render(request, 'Messenger/messenger.html',{'data':data})

def conversation(request):
    if(request.method == 'POST'):
        To = request.POST['To'] 
        request.session['to'] = To
        message = request.POST['message']
        msg = Mess(message = message, to = To, model_id = request.session.get('userId'))
        msg.save()
        return redirect('/messengermessenger')