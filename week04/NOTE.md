1、Django介绍
• Django 是一个开放源代码的Web 应用框架
• 最初用于管理劳伦斯出版集团旗下的一些以新闻内容为主的网站

2、MTV 框架模式
• 模型（Model）
• 模板（Template）
• 视图（Views）

3、django的安装和使用
Django 最新3.0 版本，目前比较多的是2.2.13（LTS）
$ pip install --upgrade django==2.2.13
>>> import django
>>> django.__version__
'2.2.13'

创建Django 项目
$ django-admin startproject MyDjango
目录结构如下：
$ find MyDjango/
MyDjango/
MyDjango/manage.py 命令行具
MyDjango/MyDjango
MyDjango/MyDjango/__init__.py
MyDjango/MyDjango/settings.py 项目的配置文件
MyDjango/MyDjango/urls.py
MyDjango/MyDjango/wsgi.py

创建Django 应用程序
$ python manage.py help 查看该工具的具体功能
$ python manage.py startapp index
index/migrations 数据库迁移文件夹
index/models.py 模型
index/apps.py 当前app 配置文件
index/admin.py 管理后台
index/tests.py 自动化测试
index/views.py 视图

启动和停止Django 应用程序
$ python manage.py runserver
默认是127.0.0.1:8000
$ python manage.py runserver 0.0.0.0:80
Quit the server with CONTROL-C
$ CONTROL-C

4、URL 调度器
MyDjango/urls.py 文件中的urlpatterns 列表，实现了：
从URL 路由到视图(views) 的映射功能
过程中使用了一个Python 模块，**URLconf**(URL configuration)，通常这个功能也被称作URLconf
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('',include('index.urls')),
]
支持正则
urls.py
re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear’),
views.py
def myyear(request, year):
return render(request, 'yearview.html')
Templates 文件夹增加yearview.html
<a href="{% url 'urlyear' 2020 %}">2020 booklist</a></div>

5、Django 快捷函数
render()
将给定的模板与给定的上下文字典组合在一起，并以渲染的文本返回一个HttpResponse 对象。
redirect()
将⼀个HttpResponseRedirect 返回到传递的参数的适当URL。
get_object_or_404()
在给定的模型管理器( model manager) 上调用get() ，但它会引发Http404 而不是模型的DoesNotExist 异常。

6、模型的处理
• 从Django 到SQL
 python manage.py makemigrations
 python manage.py migrate
• 从SQL 到Django
 python manage.py inspectdb
 
反向创建Models 
● 反向创建 Models。即根据数据库中已有的表创建映射到 Models.py 文件中 
● 1. 编辑 setting.py 文件。指定连接的数据库等相关信息。 
● 2. 执行，输出可以映射 Model 程序，使用 > 将数据流输入到指定文件中。 
○ python manage.py inspectdb 
○ 或：python manage.py inspectdb > models.py
 
7、BootStrap 模版
 ● 模板变量 {{ variables }} 
 ● 从 URL 获取模板变量 {% url 'urlyear' 2020 %} 其中 url 指定从 url中获取，‘urlyear’ 为url中的name。 
 ● 读取静态资源内容 {% static "css/header.css" %} 
 ● for 遍历标签 {% for type in type_list %} {% endfor %} 
 ● if 判断标签 {% if name.type==type.type %}{% endif %}

8、manage.py 做了些什么
1. 解析manage.py 的runserver 和IP 端口参数
2. 找到command 目录加载runserver.py
3. 检查INSTALL_APP、IP 地址、端口、ORM 对象
4. 实例化wsgiserver
5. 动态创建类并接收用户的请求











