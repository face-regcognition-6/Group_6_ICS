from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from app1 import views
from django.shortcuts import redirect

urlpatterns = [
    path('index/', views.app1, name='index'),
    path('data', views.datashow, name='data'),
    path('home/', views.home, name='home'),
    path('login/password/', views.password_login, name='password_login'),
    path('face/', views.face_login, name='face_login'),
    path('register/', views.register, name='register'),
    path('login/', lambda request: redirect('password_login')),
    path('data', views.datashow),
    path('', views.home),
    path('home', views.home),
    path('good0', views.good0),
    path('good1', views.good1),
    path('good2', views.good2),
    path('good3', views.good3),
    path('good4', views.good4),
    path('good5', views.good5),
]
