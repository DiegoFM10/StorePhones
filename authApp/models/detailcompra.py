from  django.db import models
from .user      import User
from .product   import Product

class DetailCompra(models.Model):
    id           = models.AutoField(primary_key=True) 
    user         = models.ForeignKey(User, related_name='DetaCompra_User', on_delete=models.CASCADE)
    product      = models.ForeignKey(Product, related_name='DetaCompra_Product', on_delete=models.CASCADE)          
    cantidad     = models.IntegerField(default=1)       
    valor_total  = models.IntegerField()