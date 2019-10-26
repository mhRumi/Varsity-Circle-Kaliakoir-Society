from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name = 'login'),
    path('timeline', views.timeline, name = 'timeline'),
    path('registration', views.registration, name  = 'registration'),
    path('status', views.status, name = 'status')
]

