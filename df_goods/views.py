# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.db import models

from tinymce.models import HTMLField

class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to="df_goods")
    gprice = models.DecimalField(max_digits=5, dicimal=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20, default='500g')  # 可能按箱/个买
    gclick = models.IntegerField()
    gjianjie = models.CharField(max_length=200)
    gkucun = models.IntegerField()
    gcontent = HTMLField()














