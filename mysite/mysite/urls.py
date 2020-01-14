"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('polls.urls')),
    path('registration', include('polls.urls')),
    path('timeline', include('polls.urls')),
    path('galary', include('polls.urls')),
    path('me', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('logoutUser', include('polls.urls')),
    path('login', include('polls.urls')),
    path('members', include('polls.urls')),
    path('deletePost/<int:pk>/', include('polls.urls')),
    path('comments', include('polls.urls')),
    path('viewStatus', include('polls.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

