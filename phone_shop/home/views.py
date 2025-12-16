from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
# Create your views here.
def home_page(request):
    products = Product.objects.all()
    return render(request, 'home/index.html', {'products': products})


def about(request):
    products = Product.objects.all()
    return render(request, 'home/about.html', {'products': products})

def book(request):
    products = Product.objects.all()
    return render(request, 'home/book.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'home/product_detail.html', {'product': product})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'home/product_detail.html', {'products': products})

def add_to_favorites_session(request, product_id):
    favorites = request.session.get('favorites', [])
    if product_id not in favorites:
        favorites.append(product_id)
        request.session['favorites'] = favorites
    return redirect('favorites_list')

def favorites_list_session(request):
    favorites_ids = request.session.get('favorites', [])
    products = Product.objects.filter(id__in=favorites_ids)
    return render(request, 'favorites.html', {'favorites': products})