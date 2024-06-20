from django.shortcuts import render
from shop.models import Product
# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def shop_list(request):
    product = Product.objects.get()
    data = {"Product": product}
    return render(request, 'shop/shop_list.html', context=data)