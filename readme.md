#### 开发环境介绍

##### python3.7.3 + mysql + redis + django=1.8.2 

###### 项目依赖的安装包

```
{
    Package           Version
    -irtualenv        16.6.1
    -irtualenv     16.6.1
    amqp           2.5.0
    billiard       3.5.0.5
    celery         4.0.0
    Django         1.8.2
    django-redis   4.4.0 (该版本支持django=1.8.2)
    django-tinymce 2.6.0
    itsdangerous   1.1.0
    kombu          4.6.3
    pbr            5.3.1
    Pillow         6.1.0
    pip            19.1.1
    PyMySQL        0.9.3
    pytz           2019.1
    redis          3.2.1
    setuptools     41.0.1
    six            1.12.0
    sqlparse       0.3.0
    stevedore      1.30.1
    vine           1.3.0
    wheel          0.33.4
}

```
**Django 项目搭建流程**

**django-admin startproject dailyfresh => cd dailyfresh**

**开始新建app （一个app就是一个模块）**

##### python3 manage.py startapp user  // 用户模块
##### python3 manage.py startapp goods  // 商品模块
##### python3 manage.py startapp cart // 购物车模块
##### python3 manage.py startapp order // 订单模块
######一般的 当项目模块较多 都会新建一个名为apps 的python package

**启动项目**

python3 manage.py runserver

**模型类到数据库的迁移**

python3 manage.py makemigrations   // 生成数据库库的迁移文件
python3 manage.py migrate // 执行迁移文件
（这个操作只需要在数据库有变更的时候执行）