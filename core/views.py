from django.shortcuts import render
from .models import Book, Client
from .form import Book_form, Client_form

def save_client(request):
    form = Client_form(request.POST)
    data = {}

    if form.is_valid():
        form.save()
    
    data['form'] = form

    return render(request, 'core/client.html', data)


def save_book(request):
    form = Book_form(request.POST)
    data = {}

    if form.is_valid():
        form.save()

    data['form'] = form 

    return render(request, 'core/book.html', data)    

