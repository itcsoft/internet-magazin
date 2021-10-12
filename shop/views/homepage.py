from django.shortcuts import render
from ..models import product
from ..models import category
from ..models import customer
from django.db.models import Count


def homepage(request):
    products = product.Product.objects.all()
    categories = category.Category.objects.all().annotate(products_count=Count('product'))
    customers = customer.Customer.objects.all()
    return render(request, 'index.html', {'categories':categories, 'customers':customers, 'products':products, 'all_products':products})


