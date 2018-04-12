# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ushou = models.CharField(max_length=20, default='')   # 收件人
    uaddress = models.CharField(max_length=100, default='')
    uyoubian = models.CharField(max_length=6, default='')
    uphone = models.CharField(max_length=11, default='')
    # default,blank是python层面的约束，不影响数据库表结构

