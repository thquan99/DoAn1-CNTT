from django.db import models

# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    review = models.TextField(max_length=10000, null=True)
    type = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)
    discount = models.CharField(max_length=100, null=True)
    bestSale = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title

