from django import forms
from . import models


class UserForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=16,error_messages={
        'required':'用户名不能为空',
        'max_length':'用户名过长'
    })
    password = forms.CharField(label="密码",max_length=20,error_messages={
        'required':'密码不能为空',
        'max_length':'超出规定长度'
    })
    email = forms.EmailField(label="邮箱",error_messages={
        'required':'不能为空'
    })