from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
    # ini gw tambahin
    # price = models.DecimalField(max_digits=10, decimal_places=2)

#nambahin sendiri
# class Product(models.Model):  # Mengganti 'Item' menjadi 'Product'
#     name = models.CharField(max_length=255)
#     date_added = models.DateField(auto_now_add=True)
#     amount = models.IntegerField()
#     description = models.TextField()