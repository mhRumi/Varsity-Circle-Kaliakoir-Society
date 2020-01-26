from django.urls import path
from . import views

urlpatterns = [
   path('messenger', views.messenger, name = "messenger"),
   path('conversation', views.conversation, name = "conversation")
]   