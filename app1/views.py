from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app1 import models,static
from app1.models import TestTable
from app1.models import Point




# Create your views here.

def app1(request):
    return render(request, "index.html")


def register(request):
    data = models.TestTable.objects.all()
    if request.method == 'GET':
        return render(request, "register.html", {"data": data})
    # 获取用户提交的数据
    user = request.POST.get("user")
    age = request.POST.get("age")

    # 添加到数据库
    TestTable.objects.create(name=user, age=age)

    # return HttpResponse("添加成功！")

    # 自动跳转 当跳转到非自己开发的页面时需要将域名写全
    # return redirect("http://127.0.0.1user/manage/")
    return redirect("/home")


def datashow(request):
    data = models.Point.objects.all()
    if request.method == 'GET':
        return render(request, "pages/rewards.html", {"data": data})
    # 获取用户提交的数据


    # return HttpResponse("添加成功！")

    # 自动跳转 当跳转到非自己开发的页面时需要将域名写全
    # return redirect("http://127.0.0.1user/manage/")
    return redirect("/data2/")





def home(request):
    return render(request,"home.html")

def good0(request):
    return render(request,"pages/goods/good0.html")
def good1(request):
    return render(request,"pages/goods/good1.html")
def good2(request):
    return render(request,"pages/goods/good2.html")
def good3(request):
    return render(request,"pages/goods/good3.html")
def good4(request):
    return render(request,"pages/goods/good4.html")
def good5(request):
    return render(request,"pages/goods/good5.html")
def login(request):
    return render(request, "pages/login.html")
def face2(request):
    return render(request, "pages/face.html")
# 根据id获取对应数据