from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from user.models import User
import re


# Create your views here.

# /user/register
def register(request):
    # 显示注册页面
    # print('register is coming')
    return render(request, 'register.html')


def register_handle(request):
    # print('register_handle is coming')
    print(request.POST)
    # 注册业务逻辑处理
    # 接收前端传过来的数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    # 进行数据校验
    if not all([username, password, email]):
        # 数据不完整
        return render(request, 'register.html', {'errormsg': '数据不完整'})

    # 邮箱校验
    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errormsg': '邮箱格式不正确'})

    if allow != 'on':
        return render(request, 'register.html', {'errormsg': '请同意用户协议'})

    # 进行业务逻辑处理 直接调用django本身user处理模块
    # user = User.objects.create_user(username, password, email)  // 参数位置错误
    user = User.objects.create_user(username, email, password)
    user.is_active = 0
    user.save()
    
    # 返回应答 跳转到首页
    return redirect(reverse('goods:index'))
