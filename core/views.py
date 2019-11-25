from django.shortcuts import render, redirect
from .models import Book, Client
from .form import Book_form, Client_form

def save_client(request):
    form = Client_form(request.POST)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('client_list')
    
    data['form'] = form

    return render(request, 'core/client.html', data)

def list_client (request):
    data = {}
    data['clients'] = Client.objects.all()
    
    return render(request, 'client_list.html', data) 

def update_client(request, pk):
    client = Client.objects.get(pk=pk)
    form = Client_form(request.POST or None, instance=client)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('client_list')
    
    data['form'] = form

    return render(request, 'core/client.html', data)

def delete_client(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    
    return redirect('client_list')

def save_book(request):
    form = Book_form(request.POST)
    data = {}

    if form.is_valid():
        form.save()

    data['form'] = form 

    return render(request, 'core/book.html', data)

def list_books(request):
    data = {}
    data['books'] = Book.objects.all()
    
    return render(request, data)

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = Book_form(request.POST or None, instance=book)
    data = {}

    if form.is_valid():
        form.save()
    data['form'] = form

    return render(request, data)

def delete_book(request, pk):
    book =  Book.objects.get(pk=pk)
    book.delete()

    return redirect()




