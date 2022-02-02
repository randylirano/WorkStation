from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
