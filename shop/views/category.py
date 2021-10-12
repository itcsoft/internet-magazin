from django.shortcuts import render
from ..models.product import Product
from ..models.category import Category
from django.db.models import Count


def pr_by_category(request, pk):
    all_products = Product.objects.all()
    products = Product.objects.filter(category=pk)
    categories = Category.objects.all().annotate(products_count=Count('product'))
    
    return render(request, 'index.html', {'products':products, 'categories':categories, 'all_products':all_products})
