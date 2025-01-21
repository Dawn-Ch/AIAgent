from django.shortcuts import render, HttpResponse

"""
经常用
视图函数
"""


# Create your views here.


def index(request):
    return HttpResponse("欢迎使用！")


def user_list(request):
    # 没有settings.py中的那句话，默认会去app01的目录下的templates寻找user_list.html
    # 根据app的注册顺序，逐一去他们的templates目录中找
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    # 如果是POST请求，获取用户提交的数据
    # print（request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == 'root' and password == '123':
        return HttpResponse("登陆成功")
        # return redirect("http://www.chinaunicom.com.cn/")
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})


from app01.models import Department, UserInfo


def orm(request):
    # #####  1.  新建数据
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="运营部")
    # Department.objects.create(title="IT部")

    # UserInfo.objects.create(name="陈怡霖",password="123",age=19)
    # UserInfo.objects.create(name="朱胡飞",password="666",age=29)
    # UserInfo.objects.create(name="李华",password="777",age=49)
    # UserInfo.objects.create(name="黎明乐",password="777")

    # #####  2. 删除数据
    # UserInfo.objects.filter(id=3).delete()  # fliter是筛选
    # Department.objects.all().delete()  # 删除所有数据

    # ##### 3. 获取数据
    # ##### 3.1 获取符合条件的数据
    # data_list = [对象，对象，对象]  QuerySet类型
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)

    # data_list = [对象，]
    # data_list = UserInfo.objects.filter(id=3)
    # print(data_list)

    #  ##### 3.2 获取第一条数据【对象】
    # row_obj = UserInfo.objects.filter(id=2).first()
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)

    #  ##### 4. 更新数据
    # UserInfo.objects.all().update(password=999)

    # ##### 4.1 条件更新数据
    # UserInfo.objects.filter(name="陈怡霖").update(password="666")

    return HttpResponse("成功")
