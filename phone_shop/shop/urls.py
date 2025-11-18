from django.urls import path
from .views import *

urlpatterns = [
    path('shop/', shop_page, name='shop')
]