# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse
from app1 import models
from app1.models import Point
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.contrib.auth import authenticate, login as auth_login
from django.middleware.csrf import get_token

def app1(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'GET':
        return render(request, "register.html")
    
    # 获取用户提交的数据
    student_id = request.POST.get("student_id")  # 获取学号
    name = request.POST.get("username")
    password = request.POST.get("password")
    mail = request.POST.get("mail")
    telephoneNo = request.POST.get("telephoneNo")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    face_data = request.POST.get("face_data")  # 如果表单中包含此字段
    
    # 检查学号是否已存在
    if User.objects.filter(id=student_id).exists():
        return render(request, "register.html", {"error": "该学号已注册"})

    # 加密密码
    encrypted_password = make_password(password)
    
    # 将用户数据存储到 login_user 表
    User.objects.create(
        id=student_id,  # 将学号作为 ID
        name=name,
        password=encrypted_password,
        mail=mail,
        telephoneNo=telephoneNo,
        gender=gender,
        age=age,
        face_data=face_data
    )
    
    # 注册成功，返回包含 3 秒后跳转的页面
    return render(request, 'pages/register_success.html', {'redirect_url': '/login/'})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(name=username).first()
        if user and check_password(password, user.password):
            return JsonResponse({'status': 'success', 'message': '登录成功', 'redirect_url': '/home'})
        else:
            return JsonResponse({'status': 'fail', 'message': '用户名或密码不正确'})

    csrf_token = get_token(request)
    return render(request, 'pages/login.html', {'csrf_token': csrf_token})


def datashow(request):
    data = models.Point.objects.all()
    if request.method == 'GET':
        return render(request, "pages/rewards.html", {"data": data})
    return redirect("/data2/")

def home(request):
    return render(request, "home.html")

def good0(request):
    return render(request, "pages/goods/good0.html")

def good1(request):
    return render(request, "pages/goods/good1.html")

def good2(request):
    return render(request, "pages/goods/good2.html")

def good3(request):
    return render(request, "pages/goods/good3.html")

def good4(request):
    return render(request, "pages/goods/good4.html")

def good5(request):
    return render(request, "pages/goods/good5.html")

def face2(request):
    return render(request, "pages/face.html")
