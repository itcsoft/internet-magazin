from django.shortcuts import render
from ..models.product import Product



products = []
def cartAdd(request, pk):
    product_pk = Product.objects.get(pk=pk)
    products.append(product_pk)

    return render(request, 'cart.html', {'products':products, 'product_pk':product_pk})


