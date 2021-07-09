from django.db import models

# Create your models here.
class task(models.Model):
    name = models.CharField(max_length=50, default='', editable=True)

    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
