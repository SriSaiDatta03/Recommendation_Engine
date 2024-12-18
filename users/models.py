from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(unique=True)

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)