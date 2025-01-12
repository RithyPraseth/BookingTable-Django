from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def Index(request):
    TopMenu = tblTopMenu.objects.all()
    SubTopMenu = tblSubTopMenu.objects.all()
    Sub2TopMenu = tblSub2TopMenu.objects.all()
    context ={
        'TopMenus' : TopMenu,
        'SubTopMenus' : SubTopMenu,
        'Sub2TopMenus' : Sub2TopMenu
        
    }
    return render(request, 'accounts/index.html', context)