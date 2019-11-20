from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=20, null= False)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=15, primary_key=True)
    birth = models.DateField()
    address = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length= 40, blank=False, null=False)
    author = models.CharField(max_length= 40)
