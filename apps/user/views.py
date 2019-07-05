from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

from user.models import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
import re


# Create your views here.

# /user/register
def register(request):
    # 显示注册页面
    # print('register is coming')
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 注册业务逻辑处理
        # 接收前端传过来的数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 进行数据校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 邮箱校验
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意用户协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        # 进行业务逻辑处理 直接调用django本身user处理模块
        # user = User.objects.create_user(username, password, email)  // 参数位置错误
        user = User.objects.create_user(username, email, password)
        user.is_active = 0  # 用户未激活的状态
        user.save()

        # 返回应答 跳转到首页
        return redirect(reverse('goods:index'))


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
        return render(request, 'register.html', {'errmsg': '数据不完整'})

    # 邮箱校验
    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

    if allow != 'on':
        return render(request, 'register.html', {'errmsg': '请同意用户协议'})

    # 校验用户名是否重复
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        # 用户名不存在
        user = None

    if user:
        return render(request, 'register.html', {'errmsg': '用户名已存在'})

    # 进行业务逻辑处理 直接调用django本身user处理模块
    # user = User.objects.create_user(username, password, email)  // 参数位置错误
    user = User.objects.create_user(username, email, password)
    user.is_active = 0  # 用户未激活的状态
    user.save()

    #
    # 返回应答 跳转到首页
    return redirect(reverse('goods:index'))


# 通过不同的请求方式调用该类里面不同的方法
class RegisterView(View):
    # 注册页面展示
    def get(self, request):
        return render(request, 'register.html')

    #  注册业务逻辑处理
    def post(self, request):
        # 注册业务逻辑处理
        # 接收前端传过来的数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        # 进行数据校验
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 邮箱校验
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意用户协议'})

        # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        # 进行业务逻辑处理 直接调用django本身user处理模块
        # user = User.objects.create_user(username, password, email)  // 参数位置错误
        user = User.objects.create_user(username, email, password)
        user.is_active = 0  # 用户未激活的状态
        user.save()

        # 发送激活邮件，包含激活链接: http://127.0.0.1:8000/user/active/3
        # 激活链接中需要包含用户的身份信息, 并且要把身份信息进行加密

        # 加密用户的身份信息，生成激活token
        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': user.id}
        token = serializer.dumps(info)  # 默认是bytes形式需要解码
        token = token.decode()

        # 发邮件 暂时不开启
        # subject = '天天生鲜欢迎您'
        # message = ''
        # sender = settings.EMAIL_FROM
        # receive = [email]
        # html_message = '<h1>%s, 欢迎您成为天天生鲜注册会员</h1>请点击下面链接激活您的账户<br/><a href="http://127.0.0.1:8000/user/active/%s" >http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)
        #
        # # 这是一个阻塞的过程
        # send_mail(subject, message, sender, receive, html_message=html_message)
        # 返回应答 跳转到首页
        return redirect(reverse('goods:index'))


class ActiveView(View):
    # 用户点击激活
    def get(self, request, token):
        # '进行解密 获取要激活的用户信息'
        serializer = Serializer(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            # 获取激活用户的id
            user_id = info['confirm']

            # 根据id获取用户信息
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            # 跳转到登录页面
            return redirect(reverse('user:login'))
        except SignatureExpired as e:
            # 激活链接已过期
            return HttpResponse('激活链接已过期')


class LoginView(View):
    # 登录展示页
    def get(self, request):
        return render(request, 'login.html')
