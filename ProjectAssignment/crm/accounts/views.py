from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def customer(request):
    return HttpResponse('Customer_page')

def Index(request):
    TopMenu = tblTopMenu.objects.all()
    SubTopMenu = tblSubTopMenu.objects.all()
    Sub2TopMenu = tblSub2TopMenu.objects.all()
    category = Category.objects.all()
    Menu = tblFoodMenu.objects.all()
    context ={
        'TopMenus' : TopMenu,
        'SubTopMenus' : SubTopMenu,
        'Sub2TopMenus' : Sub2TopMenu,
        'FoodCategory' : category,
        'FoodMenu' : Menu        
    }
    return render(request, 'accounts/index.html', context)
    
