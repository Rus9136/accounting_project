from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Category, Expense

admin.site.register(Category)
admin.site.register(Expense)

