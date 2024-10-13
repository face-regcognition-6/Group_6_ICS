from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
import cv2
from insightface.app import FaceAnalysis
import numpy as np
from PIL import Image
from django.contrib.auth.hashers import make_password, check_password

from app1 import models

# 初始化人脸分析模型
app = FaceAnalysis(providers=['CUDAExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

def password_login(request):
    if request.method == 'POST':
        # 模拟直接登录成功，不做验证
        return JsonResponse({'status': 'success', 'message': '登录成功', 'redirect_url': '/home'})
    
    return render(request, 'password_login.html')

# 人脸登录视图
def face_login(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'success', 'message': '登录成功', 'redirect_url': '/home'})
    
    # 返回人脸登录页面
    return render(request, 'face_login.html')

# # 密码登录视图
# def password_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # 处理密码登录
#         user = User.objects.filter(name=username).first()
#         if user:
#             if check_password(password, user.password):
#                 print(f"Logging in user: {user.name}, ID: {user.pk}")
#                 auth_login(request, user)
#                 return JsonResponse({'status': 'success', 'message': '登录成功', 'redirect_url': '/home'})
#             else:
#                 return JsonResponse({'status': 'fail', 'message': '密码不正确'})
#         else:
#             return JsonResponse({'status': 'fail', 'message': '用户名不存在'})

#     return render(request, 'password_login.html')


# def face_login(request):
#     if request.method == 'POST':
#         profile_picture = request.FILES.get('profile_picture')

#         if profile_picture:
#             try:
#                 # 打印图片信息，确保文件上传正常
#                 print(f"Profile picture name: {profile_picture.name}, size: {profile_picture.size}")

#                 # 处理上传的照片，提取人脸特征向量
#                 image = Image.open(profile_picture)
#                 image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)  # 转换为OpenCV的BGR格式
#                 faces = app.get(image)

#                 if faces:
#                     face = faces[0]
#                     embedding = face.normed_embedding

#                     # 查询数据库中已存储的用户人脸特征向量
#                     users = User.objects.exclude(face_data__isnull=True)
#                     for user in users:
#                         stored_embedding = np.fromstring(user.face_data, sep=',')
#                         similarity = np.dot(stored_embedding, embedding) / (
#                                 np.linalg.norm(stored_embedding) * np.linalg.norm(embedding))

#                         if similarity > 0.5:
#                             auth_login(request, user)
#                             return JsonResponse({'status': 'success', 'message': '人脸识别登录成功', 'redirect_url': '/home'})

#                     return JsonResponse({'status': 'fail', 'message': '人脸匹配失败，未找到对应用户'})
#                 else:
#                     return JsonResponse({'status': 'fail', 'message': '未检测到人脸，请上传清晰的正面照片'})
#             except Exception as e:
#                 # 打印详细的错误日志，以便进一步调试
#                 print(f"Error processing profile picture: {e}")
#                 return JsonResponse({'status': 'fail', 'message': f'图片处理失败: {str(e)}'})

#     return render(request, 'face_login.html')


# 注册视图
def register(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')  # 学号作为ID
        username = request.POST.get('username')  # 用户名
        password = request.POST.get('password')  # 密码
        email = request.POST.get('mail')  # 邮箱
        telephoneNo = request.POST.get('telephoneNo')  # 电话号码
        gender = request.POST.get('gender')  # 性别
        age = request.POST.get('age')  # 年龄
        profile_picture = request.FILES.get('profile_picture')  # 上传的照片

        # 检查是否上传了照片
        if not profile_picture:
            return render(request, 'register.html', {'error': '请上传照片'})

        # 处理照片并提取人脸特征向量
        try:
            image = Image.open(profile_picture)
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            faces = app.get(image)

            if faces:
                face = faces[0]
                embedding = face.normed_embedding
                face_data = ','.join(map(str, embedding.tolist()))  # 转换为字符串并存储人脸特征
            else:
                return render(request, 'register.html', {'error': '未检测到人脸，请上传清晰的正面照片'})
        except Exception as e:
            return render(request, 'register.html', {'error': f'图片处理失败: {str(e)}'})

        # 加密密码并存储用户信息
        encrypted_password = make_password(password)
        try:
            user = User.objects.create(
                id=student_id,  # 学号作为用户ID
                name=username,
                password=encrypted_password,
                mail=email,
                telephoneNo=telephoneNo,
                gender=gender,
                age=age,
                face_data=face_data  # 存储人脸特征数据
            )
        except Exception as e:
            return render(request, 'register.html', {'error': '注册过程中出现错误，请稍后再试'})

        # 注册成功后重定向到首页或登录页
        return redirect('index')

    return render(request, 'register.html')


# 主页视图
def home(request):
    return render(request, 'home.html')


# 数据展示视图
def datashow(request):
    data = models.Point.objects.all()
    if request.method == 'GET':
        return render(request, "pages/rewards.html", {"data": data})
    return redirect("/data2/")


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
    return render(request, "face_login.html")

def app1(request):
    return render(request, "index.html")
