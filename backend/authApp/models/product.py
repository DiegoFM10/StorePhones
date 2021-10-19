from django.db import models
from .user import User

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField('Marca',max_length = 25)
    modelo = models.CharField('Modelo', max_length = 25)
    