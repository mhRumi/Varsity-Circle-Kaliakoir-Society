from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name = 'login'),
    path('timeline', views.timeline, name = 'timeline'),
    path('registration', views.registration, name  = 'registration'),
    path('status', views.status, name = 'status'),
    path('galary', views.galary, name = 'galary'),
    path('me', views.me, name = 'name'),
    path('login', views.login, name = 'login'),
    path('logoutUser', views.logoutUser, name = 'logoutUser'),
    path('members', views.members, name = 'members'),
    path('deletePost/<int:pk>/', views.deletePost, name = 'deletePost'),
    path('comments', views.comments, name = 'comments'),
    path('viewStatus', views.viewStatus, name = 'viewStatus'),
]

