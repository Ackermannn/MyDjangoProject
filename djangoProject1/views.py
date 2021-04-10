#! usr/bin/env python3
import os

from django.http import HttpResponse, FileResponse

# https://www.runoob.com/django/django-first-app.html
from django.shortcuts import render
from datetime import datetime
import pytz
from djangoProject1.settings import BASE_DIR


def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'runoob.html', context)


def pivot(request):
    context = {"msg": ""}
    if request.method == "POST":
        File = request.FILES.get("filename", None)
        if File is None:
            return HttpResponse("请选择需要上传文件")
        else:

            with open(f"./data.csv", 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            context["msg"] = "上传成功! 下载文件 获取结果"
            from .pan20Utill.preprocess import preprocessCSV
            preprocessCSV("./data.csv", "./data.csv")
            return render(request, 'pivot.html', context)  #

    return render(request, 'pivot.html', context)


def download(request):
    file = open('./data.csv', 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="data.csv"'
    return response


def viewPass(request):
    # context = {'hello': 'Hello World!'}
    return render(request, 'pass.html')

from django.utils import timezone
def fakecode(request):
    # context = {'hello': 'Hello World!'}
    if request.method == "GET" and request.GET:
        id = request.GET.get("id")
        name = request.GET.get("name")
        local = request.GET.get("local")
        tz = pytz.timezone('Asia/Shanghai')
        return render(request, 'pass.html', context={
            "id": id,
            "name": name,
            "local": local,
            "date": datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        })
    return render(request, 'fakecode.html')


def index(request):
    return render(request, 'index.html')
