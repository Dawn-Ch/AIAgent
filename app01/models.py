from django.db import models

"""
对数据库进行操作
以前用pymysql，但Django不用pymysql
Django封装了ORM，直接使用
"""


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)


class Department(models.Model):
    title = models.CharField(max_length=16)


# ###########  新建数据  #################
# 本质：新建数据  insert into app01_department(title)values("销售部")
# Department.objects.create(title="销售部")
# UserInfo.objects.create(name="chenyilin", password="123", age=19)

# class Role(models.Model):
#     caption = models.CharField(max_length=16)
