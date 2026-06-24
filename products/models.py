
from django.db import models
class Product(models.Model):
    product_name=models.CharField(max_length=255,db_index=True)
    product_description=models.TextField()
    category=models.CharField(max_length=100,db_index=True)
    tags=models.TextField()
