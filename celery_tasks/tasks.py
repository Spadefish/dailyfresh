from django.core.mail import send_mail
from django.conf import settings
from celery import Celery
import time

# 在任务处理者一端（ubuntu下面）加这几句
# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
# django.setup()

# 创建一个celery类的实例对象
app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/8')


# 定义任务函数
@app.tesk
def send_register_active_email(to_email, username, token):
    # 发送激活邮件
    subject = '天天生鲜欢迎您'
    message = ''
    sender = settings.EMAIL_FROM
    receive = [to_email]
    html_message = '<h1>%s, 欢迎您成为天天生鲜注册会员</h1>请点击下面链接激活您的账户<br/><a href="http://127.0.0.1:8000/user/active/%s" >http://127.0.0.1:8000/user/active/%s</a>' % (
    username, token, token)

    # 这是一个阻塞的过程
    send_mail(subject, message, sender, receive, html_message=html_message)
    time.sleep(5)
