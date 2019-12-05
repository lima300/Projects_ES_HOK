from django.forms import ModelForm
from .models import *

class Client_form(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'cpf', 'birth', 'address']

class Book_form(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'discription', 'price', 'author', 'publisher']

class Cupom_form(ModelForm):
    class Meta:
        model =  Cupom
        fields = ['name', 'discount']

class Sale_form(ModelForm):
    class Meta:
        model = Sale
        exclude = ['price']

class Employee_form(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


