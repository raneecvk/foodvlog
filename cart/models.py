from django.db import models
from shop.models import *

# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=100,unique=True)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class items(models.Model):

    prodt=models.ForeignKey(products,on_delete=models.CASCADE)

    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    active=models.BooleanField(default=True)

    quandity=models.IntegerField()

    def __str__(self):
        return str(self.prodt)
    def total(self):
        return self.prodt.price*self.quandity