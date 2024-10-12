# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse
from app1 import models
from django.contrib.auth.hashers import make_password, check_password
from .models import User,Point
from django.contrib.auth import login as auth_login
from django.middleware.csrf import get_token
import cv2
from insightface.app import FaceAnalysis
import numpy as np
from PIL import Image
import io
import logging
from django.utils import timezone

def app1(request):
    return render(request, "index.html")

# 初始化人脸分析模型
app = FaceAnalysis(providers=['CUDAExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

logger = logging.getLogger(__name__)

def register(request):
    # Log the start of the request processing
    logger.debug("Start processing registration request")

    if request.method == 'GET':
        return render(request, "register.html", {"error": None})

    # 获取用户提交的数据
    student_id = request.POST.get("student_id")
    name = request.POST.get("username")
    password = request.POST.get("password")
    mail = request.POST.get("mail")
    telephoneNo = request.POST.get("telephoneNo")
    gender = request.POST.get("gender")
    age = request.POST.get("age")

    logger.debug(f"Received form data: student_id={student_id}, name={name}, mail={mail}, phone={telephoneNo}")

    # 获取上传的照片文件
    profile_picture = request.FILES.get("profile_picture")
    if not profile_picture:
        logger.error("No profile picture uploaded")
        return render(request, "register.html", {"error": "请上传照片"})

    # 检查学号是否已存在
    if User.objects.filter(id=student_id).exists():
        logger.error(f"User with student_id {student_id} already exists")
        return render(request, "register.html", {"error": "该学号已注册"})

    # 加密密码
    encrypted_password = make_password(password)
    logger.debug("Password encrypted")

    # 处理上传的照片，提取人脸特征向量
    try:
        # 将上传的图片文件转换为OpenCV可处理的格式
        image = Image.open(profile_picture)
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  # 转换为OpenCV的BGR格式
        logger.debug("Profile picture loaded and converted for face detection")
    except Exception as e:
        logger.error(f"Error processing profile picture: {e}")
        return render(request, "register.html", {"error": "图片处理失败，请上传正确格式的照片"})

    # 使用insightface提取人脸特征值
    faces = app.get(image)
    if faces:
        face = faces[0]  # 假设只有一个人脸
        embedding = face.normed_embedding
        logger.debug(f"Extracted embedding: {embedding}")

        # 将嵌入向量转换为字符串格式存储
        face_data = ','.join(map(str, embedding.tolist()))
    else:
        logger.error("No face detected in the uploaded image")
        return render(request, "register.html", {"error": "未检测到人脸，请上传清晰的正面照片"})

    # 存储用户信息到数据库
    try:
        user = User.objects.create(
            id=student_id,
            name=name,
            password=encrypted_password,
            mail=mail,
            telephoneNo=telephoneNo,
            gender=gender,
            age=age,
            face_data=face_data  # 存储提取的人脸特征值
        )
        logger.info(f"User {user.id} successfully registered with face data")

        # 更新 last_login 字段
        user.update_last_login()

        # 自动登录用户
        auth_login(request, user)
        return render(request, 'pages/register_success.html', {'redirect_url': '/login/'})
    except Exception as e:
        logger.error(f"Error saving user to database: {e}")
        return render(request, "register.html", {"error": "注册过程中出现错误，请稍后再试"})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        profile_picture = request.FILES.get('profile_picture')

        if username and password:
            # 处理用户名和密码登录
            user = User.objects.filter(name=username).first()
            if user and check_password(password, user.password):
                auth_login(request, user)
                return JsonResponse({'status': 'success', 'message': '登录成功', 'redirect_url': '/home'})
            else:
                return JsonResponse({'status': 'fail', 'message': '用户名或密码不正确'})

        if profile_picture:
            try:
                # 处理上传的照片，提取人脸特征向量
                image = Image.open(profile_picture)
                image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  # 转换为OpenCV的BGR格式
                faces = app.get(image)

                if faces:
                    face = faces[0]
                    embedding = face.normed_embedding
                    logger.debug(f"Extracted embedding: {embedding}")

                    # 将嵌入向量与数据库中用户的人脸特征向量进行匹配
                    users = User.objects.exclude(face_data__isnull=True)  # 查询所有有存储人脸特征的用户
                    for user in users:
                        stored_embedding = np.fromstring(user.face_data, sep=',')
                        similarity = np.dot(stored_embedding, embedding) / (np.linalg.norm(stored_embedding) * np.linalg.norm(embedding))

                        if similarity > 0.9:  # 假设0.9为匹配阈值
                            auth_login(request, user)
                            return JsonResponse({'status': 'success', 'message': '人脸识别登录成功', 'redirect_url': '/home'})

                    return JsonResponse({'status': 'fail', 'message': '人脸匹配失败，未找到对应用户'})
                else:
                    return JsonResponse({'status': 'fail', 'message': '未检测到人脸，请上传清晰的正面照片'})
            except Exception as e:
                logger.error(f"Error processing profile picture: {e}")
                return JsonResponse({'status': 'fail', 'message': '图片处理失败，请稍后再试'})

    return render(request, 'pages/login.html')


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
