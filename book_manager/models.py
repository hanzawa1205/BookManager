from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager



class Book(models.Model):
    name=models.CharField(max_length=100,null=False)
    author=models.CharField(max_length=100,null=False)
    content = models.TextField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '图书信息'
        verbose_name_plural = verbose_name
        db_table="BOOK"

    def __unicode__(self):
        return self.name


class User(models.Model):
    username=models.CharField("用户名",max_length=100)
    password=models.CharField("密码",max_length=100)
    email = models.EmailField("邮箱")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        db_table="User"

    def __unicode__(self):
        return self.username


