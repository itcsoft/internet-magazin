from django.db import models
from .category import Category
from .customer import Customer
from .product import Product
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    phone = models.CharField(max_length=20, default='', blank=True)
    address = models.CharField(max_length=255, default='', blank=True)
    date = models.DateField(auto_now_add=datetime.datetime.today)
    status = models.BooleanField(default=False)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
