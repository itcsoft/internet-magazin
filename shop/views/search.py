from django.shortcuts import render, redirect
from ..models.product import Product
from ..views import category
from django.db.models import Count



def search(request):
    if request.method == "POST":
        searched_product_from_input = request.POST.get('searched_product').title()
        print(searched_product_from_input)
        searched_products = Product.objects.filter(name__contains=searched_product_from_input)
        categories = category.Category.objects.all().annotate(products_count=Count('product'))
        products = Product.objects.all()


        return render(request, 'search.html', {'searched_product_from_input':searched_product_from_input, 'searched_products':searched_products, 'categories':categories, 'all_products':products })