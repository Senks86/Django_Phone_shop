from django.shortcuts import render
from .models import Product
# Create your views here.
def home_page(request):
    products = Product.objects.all()
    return render(request, 'home/index.html', {'products': products})
