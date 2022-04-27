from django.db import models
from shop.models import *
from django.contrib.auth.models import User
# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return '{}' .format(self.cart_id)
class items(models.Model):
    prodt=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return '{}' .format(self.prodt)
    def total(self):
        return self.prodt.price*self.quan
