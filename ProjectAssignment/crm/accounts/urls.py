from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Index),
    path('api/book-a-table/', book_table, name='book_table'),
]