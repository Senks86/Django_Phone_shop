from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', home_page, name='home'),
    path('book/', views.book, name='book_table'),
    path('about/', views.about, name='about'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail')
]


