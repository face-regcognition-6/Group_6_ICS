"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from app1 import views
urlpatterns = [
    path('index/', views.app1),
    path('register/', views.register),
    path('data', views.datashow),
    path('', views.home),
    path('home', views.home),
    path('good0', views.good0),
    path('good1', views.good1),
    path('good2', views.good2),
    path('good3', views.good3),
    path('good4', views.good4),
    path('good5', views.good5),
    path('login/', views.login),
    path('face/', views.face2),
    path('video/', include('video.urls')),
]
