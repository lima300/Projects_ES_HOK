from django.forms import ModelForm
from .models import Book, Client

class Client_form(ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'cpf', 'birth', 'address']

class Book_form(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']