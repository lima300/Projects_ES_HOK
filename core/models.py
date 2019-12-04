from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=20, null= False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=15, unique=True)
    birth = models.DateField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length= 40, blank=False, null=False, unique=True)
    discription = models.CharField(max_length=200, blank=False, null=False)
    price = models.FloatField(default=0)
    author = models.CharField(max_length= 40)
    publisher = models.CharField(max_length=40)

    def __str__(self):
        return self.title

class Cupom(models.Model):
    name = models.CharField(max_length=10, unique=True)
    discount = models.FloatField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=20, null= False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=10, blank=False, null=False)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class Sale(models.Model):
    book = models.ForeignKey(Book,on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    cupom = models.ForeignKey(Cupom, on_delete=models.PROTECT, blank=True, null=True)
    price = models.FloatField()
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)



