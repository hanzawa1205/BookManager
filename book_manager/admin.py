from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('name','author','content','price','date')




admin.site.register(Book,BookAdmin)

