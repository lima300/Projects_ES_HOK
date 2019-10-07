from django.shortcuts import render
from .models import Book
from .form import Book_form

def save_book(request):
    form = Book_form(request.POST)
    data = {}

    if form.is_valid():
        form.save()

    data['form'] = form 

    return render(request, 'core/book.html', data)    

