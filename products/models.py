from django.db import models


class Product(models.Model):

    Name = models.CharField(max_length=225)
    Description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    slug = models.SlugField()

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


