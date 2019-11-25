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

class Sale(ModelForm):
    class Meta:
        model = Sale
        fields = ['book','client', 'cupom']


