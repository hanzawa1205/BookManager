"""bm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_book/',views.get_books,name='get_books'),
    path('',views.login),
    path('register/',views.register_view),
    path('logout/',views.logout),
    path('setpw/',views.set_password),
    path('add_book/',views.add_book),
    path('book_detail/',views.book_detail,name='book_detail'),
    path('book_delete/',views.book_delete,name='book_delete'),
    path('search/',views.search,name='search'),
    path('edit/',views.edit,name='edit'),
    path('forget_pw/',views.forget_pw,name='forget_pw'),
    path('new_pw/',views.new_pw,name='new_pw'),
    path('register_c/',views.register_check)
]
