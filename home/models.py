
from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    

class Supplier(models.Model):
    SupplierName = models.CharField(max_length=100)
    Product = models.CharField(max_length=50)
    Category = models.CharField(max_length=50)
    BuyingPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ContactNumber = models.CharField(max_length=15)
    Email = models.EmailField(max_length=100)  # ✅ أضفنا ده
    Type = models.CharField(
        max_length=20,
        choices=[
            ('Taking return', 'Taking return'),
            ('Not taking return', 'Not taking return')
        ]
    )

    def __str__(self):
        return self.SupplierName

class Order(models.Model):
    product_name = models.CharField(max_length=100)
    product_id = models.IntegerField()
    category = models.CharField(max_length=100)
    order_value = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_of_delivery = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} ({self.product_id})"
    


class ManageStore(models.Model):
    location = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    manager_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.street}"