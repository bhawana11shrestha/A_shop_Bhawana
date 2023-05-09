from django.db import models
from base.models import BaseModel #importing model from the base file

class Category(BaseModel):
    category_name = models.models.CharField(max_length=100)
    category_image = models.models.ImageField(upload = "categories")

class Product(BaseModel):
    product_name = models.models.CharField(_(""), max_length=100)
    category = models.ForeignKey(category, on_delete = models.CASCADE, related_name="products")
    prict = models.IntegerField()


class ProductImage(BaseModel):
    product = models.models.ForeignKey(product,on_delete=models.CASCADE,related_name="product_image")
    image = models.ImageField(upload="product")