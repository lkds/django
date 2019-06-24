from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
#定向到登录
def login(request):
    return render(request,'login.html')

#注册页面
def register(request):
    return render(request,'register.html')

#登录校验
def loginres(request):
    acount = request.GET.get('acount',0)
    passwd = request.GET.get('password',0)
    if acount=='' or passwd =='':
        return HttpResponse('账号或者密码为空！')
#注册校验
def registerres(request):
    acount = request.GET.get('acount',0)
    passwd = request.GET.get('password',0)
    cofirmpass = request.GET.get('cofirmpass',0)
    nickname = request.GET.get('nickname',0)
    gender = request.GET.get('gender',0)
    city = request.GET.get('city',0)
    motto = request.GET.get('motto',0)
    if acount == '' or passwd == '' or cofirmpass == '' or nickname =='' or gender == '' or city == '' or motto == '':
        return HttpResponse('请完整填写！')
    elif passwd != cofirmpass:
        return HttpResponse('两次密码不一致！')
    else:
        return HttpResponse('注册成功！')
    