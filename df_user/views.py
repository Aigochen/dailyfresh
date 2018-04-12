# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from hashlib import sha1
from models import *

# Create your views here.
# 注册页面
def register(request):
    return render(request, 'df_user/register.html')

    # 接收用户输入
def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码
    if upwd != upwd2:
        return redirect('/user/register/')  # 重定向到register页面
    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd2 = s1.hexdigest()

    # 创建对象,添加数据
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd2
    user.uemail = uemail
    user.save()
    # 注册成功，转到登录页面
    return redirect('/user/login/')

# 检查用户是否已经存在
from django.http import JsonResponse  # 继承响应
def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})
    # 'count':count 为 键值对

# 登录页面
def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'df_user/login.html', context)

# 登录处理
from django.http import HttpResponseRedirect
def login_handle(request):
    # 接收请求信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)  # 0位默认值，如login.html中jizhu的value=0，则记住的get接收默认属性0
    # 根据用户名查询对象
    users = UserInfo.objects.filter(uname=uname)
    print uname
    # 判断：如果未查询到用户名则错，如果查询到则判断密码是否正确，正确则转到用户中心
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            # 记住用户名
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录', 'error_name':0, 'error_pwd':1, 'uname':uname, 'upwd': upwd }
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name':1, 'error_pwd':0, 'uname': uname, 'upwd': upwd }
        return render(request, 'df_user/login.html', context)

#  用户中心 个人信息
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    context = {'title': '用户中心',
               'user_email': user_email,
               'user_name': request.session['user_name']}
    return render(request, 'df_user/user_center_info.html', context)

#  订单信息
def order(request):
    context = {'title': '用户中心'}
    return render(request, 'df_user/user_center_order.html', context)

# 收货地址
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '用户中心', 'user': user}
    return render(request, 'df_user/user_center_site.html', context)
