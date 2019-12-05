from django.shortcuts import render, redirect
from .models import *
from .form import *

def save_client(request):
    form = Client_form(request.POST)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('client_list')
    
    data['form'] = form

    return render(request, 'core/InserirCliente.html', data)

def list_client (request):
    data = {}
    data['clients'] = Client.objects.all()
    
    return render(request, 'core/ManterClientes.html', data) 

def update_client(request, pk):
    client = Client.objects.get(pk=pk)
    form = Client_form(request.POST or None, instance=client)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('client_list')
    
    data['form'] = form

    return render(request, 'core/AlterarClientes.html', data)

def delete_client(request, pk):
    client = Client.objects.get(pk=pk)
    client.delete()
    
    return redirect('client_list')

def read_client(request):
    if request.POST:
        cpf = request.POST['cpfCliente']
        user = Client.objects.get(cpf=cpf)
        data = {'client' : user}
        return render(request, 'core/client.html', data)
    
    return render(request, 'core/BuscarCliente.html')

def save_book(request):
    form = Book_form(request.POST)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('livros')

    data['form'] = form 

    return render(request, 'core/InserirProduto.html', data)

def list_books(request):
    data = {}
    data['books'] = Book.objects.all()
    
    return render(request, 'core/ManterProdutos.html', data)

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

    return redirect('livros')

def save_cupom(request):
    form = Cupom_form(request.POST)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('cupons')
    
    data['form'] = form

    return render(request, 'core/InserirCupom.html', data)

def list_cupom(request):
    data = {}
    data['cupons'] = Cupom.objects.all()
    
    return render(request, 'core/ManterCupons.html', data)


def delete_cupom(request, pk):
    cupom =  Cupom.objects.get(pk=pk)
    cupom.delete()

    return redirect('cupons')


def save_employee(request):
    form = Employee_form(request.POST)
    data = {}

    if form.is_valid():
        form.save()
        return redirect ('login')

    data['form'] = form 

    return render(request, 'core/Cadastro.html', data)

def delete_employee(request, pk):
    emp =  Employee.objects.get(pk=pk)
    emp.delete()

    return redirect()

def save_sale(request):
    form = Sale_form(request.POST)
    data = {}
    print(1)
    if form.is_valid():
        object = form.save(commit=False)
        if object.cupom is None:
            object.price = object.book.price
        else:
            object.price = (1-object.cupom.discount) * object.book.price
        object.save()
        data['sales'] = Sale.objects.all()
        return render(request, 'core/ManterVendas.html', data)

    data['form'] = form 

    return render(request, 'core/InserirVendas.html', data)

def update_sale(request, pk):
    sale = Sale.objects.get(pk=pk)
    form = Sale_form(request.POST or None, instance=sale)
    data = {}

    if form.is_valid():
        form.save()
        data['sales'] = Sale.objects.all()
        return render(request, 'core/ManterVendas.html', data )

    data['form'] = form

    return render(request, 'core/AlterarVendas.html', data)

def delete_sale(request, pk):
    sale =  Sale.objects.get(pk=pk)
    sale.delete()
    
    data = {}
    data['sales'] = Sale.objects.all()

    return render(request, 'core/ManterVendas.html', data)

def menu(request):
    return render(request, 'core/Menu.html')

def login(request):
    if request.POST:
        email = request.POST['email_login']
        senha = request.POST['senha_login']

        usuario = Employee.objects.get(email=email)

        if(senha == usuario.password):
            return redirect('menu')


    return render(request, 'core/Login.html')

def menuClient(request):
    return render(request, 'core/MenuClientes.html')

def menuVendas(request):
    return render(request, 'core/MenuVendas.html')

def menuLivro(request):
    return render(request, 'core/MenuProdutos.html')

def menuCupom(request):
    return render(request, 'core/MenuCupons.html')

def menuFunc(request):
    return render(request, 'core/MenuFuncionarios.html')

def read_sale(request):
    if request.POST:
        func = Employee.objects.get(cpf=request.POST['cpfFuncionario'])
        sales = Sale.objects.filter(employee=func)

        data = {'sales' : sales}

        return render(request, 'core/ManterVendas.html', data)
    
    return render(request, 'core/BuscarVendas.html')

def read_book(request):
    if request.POST:
        book = Book.objects.get(title=request.POST['NomeProduto'])
        data = {'book' : book}

        return render(request, 'core/book.html', data)
    
    return render(request, 'core/BuscarProduto.html')

def read_cupom(request):
    if request.POST:
        cupom = Cupom.objects.get(name=request.POST['nomeCupom'])
        data = {'cupom' : cupom}

        return render(request, 'core/cupom.html', data)
    
    return render(request, 'core/BuscarCupons.html')

def read_func(request):
    if request.POST:
        emp = Employee.objects.get(cpf=request.POST['cpfFuncionario'])
        data = {'func' : emp}

        return render(request, 'core/ManterFuncionarios.html', data)
    
    return render(request, 'core/BuscarFuncionarios.html')

def delete_func(request, pk):
    func = Employee.objects.get(pk=pk)

    func.delete()

    return redirect('menu')


