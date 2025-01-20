from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import BookTableSerializer
from rest_framework import status
from rest_framework.response import Response
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
    
@api_view(['POST'])
def book_table(request):
    if request.method == 'POST':
        serializer = BookTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Booking successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)