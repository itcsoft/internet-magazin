from django.shortcuts import render
from ..models import product

def detail(request, pk):
    product_pk = product.Product.objects.get(pk=pk)
    products = product.Product.objects.all()
    return render(request, 'detail.html',{'product_pk':product_pk, 'products':products})