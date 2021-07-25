from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=64,unique=True)

class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=64,unique=True)
    category = models.ForeignKey(Category,models.SET_NULL,blank=True,null=True,)

class Product(models.Model):
    product_name = models.CharField(max_length=64,unique=True)
    sub_category = models.ForeignKey(SubCategory,models.SET_NULL,blank=True,null=True,)


