from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class products(models.Model):

    STATUS = (

              ('PharmaceuticalDrugs', 'PharmaceuticalDrugs'),
              ('Tradomedicals', 'Tradomedicals'),
              ('skincare', 'skincare'),
    )

    item = models.CharField(max_length=200)
    price = models.IntegerField()
    product_no = models.CharField(max_length=200)
    status = models.CharField(max_length=300, choices=STATUS, null=True)

    def __str__(self):
        return self.item

class customers(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    Tel = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    profile_Pic = models.ImageField(null=True, default="imageo1.jpg", blank=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name


class customer_orders(models.Model):

     customer_name = models.CharField(max_length=30)
     product_name = models.ForeignKey(products, null=True, max_length=30, on_delete=models.SET_NULL)
     Quantity = models.IntegerField()
     Amount = models.IntegerField()
     Email = models.CharField(max_length=30)
     customers_address = models.CharField(max_length=30)
     dateCreated = models.DateTimeField(auto_now_add=True, null=True)

     def __str__(self):
         return self.product_name


class adminEntry(models.Model):

    STATUS = (
        ('Delivered', 'Delivered'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Pending', 'Pending'),
    )

    customer_firstname = models.ForeignKey(customers, null=True, max_length=30, on_delete=models.SET_NULL)
    status = models.CharField(max_length=30,null=True, choices=STATUS)
    Item = models.ForeignKey(products, null=True, max_length=30, on_delete=models.SET_NULL)
    Quantity = models.IntegerField()
    Amount = models.IntegerField()
    Phone = models.CharField(max_length=30)
    customers_address = models.CharField(max_length=30)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Item.item








