from django.forms import ModelForm
from .models import Book

class Book_form(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']