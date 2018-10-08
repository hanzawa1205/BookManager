from django.shortcuts import render,render_to_response,redirect
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import time
# Create your views here.

@login_required()
def get_books(request):
    books = Book.objects.all()
    ctx ={
        'books':books,
        'username':request.user.username
    }
    return render (request, 'get_book.html',ctx )


def register_view(request):
        if request.method == 'POST':
            username = request.POST.get("username",'')
            password = request.POST.get("password",'')
            email = request.POST.get("email",'')
            user = User.objects.create_user(username=username,password=password,email=email)
            print(user)
            user.save()
            return redirect("/")
        return render(request, 'register.html')


def register_check(request):
        if request.method=="POST":
            name = request.POST.get("name")
            print(name)
            ret = User.objects.get(username=name)
            if ret:
                 msg ="用户名已被注册!"
            else:
                msg = ""
            return HttpResponse(msg)



def login(request):
    err_msg = ''
    if request.method=='POST':
        username = request.POST.get("username",'')
        password = request.POST.get("password",'')
        print(username,password)
        user = auth.authenticate(username=username , password=password)
        if user:
            auth.login(request,user) #把user封装到request里面，方便后面调用
            return redirect("/get_book/")
        else:
            err_msg= '用户名或密码错误'
    context = {
                'err_msg':err_msg,
               }
    return render(request,'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required()
def set_password(request):
    user = request.user
    err_msg = ''
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                err_msg = '新密码不能为空'
            elif new_password != repeat_password:
                err_msg = '两次密码不一致'
            else:
                user.set_password(new_password)
                user.save()
                return redirect("/")
        else:
            err_msg = '原密码输入错误'
    content = {
        'err_msg': err_msg,
    }
    return render(request, 'setpw.html', content)


@login_required()
def add_book(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        book_author = request.POST.get('book_author')
        book_price = request.POST.get('book_price')
        # book_content = request.POST.get('book_content')
        if book_name and book_author and book_price is not None:
            book=Book.objects.create(name=book_name,author=book_author,price=book_price)
            book.save()
            return redirect('/get_book')
    return render(request,'add_book.html')

@login_required()
def book_detail(request):
    book_id = request.GET.get('id')
    book=Book.objects.get(id=book_id)
    return render(request,'book_detail.html',{'book':book})


def book_delete(request):
        delete_id= request.POST.get("id")
        print(id)
        book=Book.objects.get(id=delete_id)
        book.delete()
        return HttpResponse("删除成功")


def search(request):
    if request.method=='POST':
        s_n = request.POST.get('book_name')
        s_b =Book.objects.get(name=s_n)
        return render(request,'get_book.html',{'s_b':s_b})

@login_required()
def edit(request):
    id = request.GET.get("id")
    if request.method == 'GET':
        obj = Book.objects.filter(id=id).first()
        return render(request, 'edit.html', {'obj': obj})
    elif request.method == 'POST':
        id = request.POST.get('edit_id')
        name = request.POST.get('edit_name')
        author = request.POST.get('edit_author')
        content = request.POST.get('edit_content')
        price = request.POST.get('edit_price')
        new_book = Book.objects.get(id=id)
        new_book.name = name
        new_book.author = author
        new_book.content=content
        new_book.price =price
        new_book.save()
        return redirect('/get_book/')


def forget_pw(request):
        if request.method == 'POST':
            un = request.POST.get('username')
            em = request.POST.get('r_email')
            obj = User.objects.get(username=un)
            if obj.email == em:
                return redirect('/new_pw/')
        return render(request,'forget_pw.html')


def new_pw(request):
    err_msg = ''
    if request.method == 'POST':
        un = request.POST.get('username')
        print(un)
        new_password = request.POST.get('new_password')
        print(new_password)
        re_password = request.POST.get('repeat_password')
        print(re_password)
        user = User.objects.get(username=un)
        if new_password == re_password:
            user.set_password(new_password)
            user.save()
            return redirect('/')
        else:err_msg='两次密码不一致'
    return render(request,'new_pw.html',{'err_msg':err_msg})

