from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('book/', save_book, name='save_book'),
    path('client/', save_client, name='save_client'),
    path('updateC/<int:pk>/', update_client, name='update_client'),
    path('deleteC/<int:pk>/', delete_client, name='delete_client'),
    path('clients/',list_client, name='client_list'),
    path('cupom/', save_cupom, name='save_cupom'),
    path('employee/', save_employee, name='save_employee'),
    path('sale/', save_sale, name='save_sale'),
    path('deleteCm/<int:pk>/', delete_cupom, name='delete_cupom'),
    path('deleteE/<int:pk>/', delete_employee, name='delete_employee'),
    path('deleteS/<int:pk>/', delete_sale, name='delete_sale'),
    path('updateS/<int:pk>/', update_sale, name='update_sale'),
    path('menu/', menu, name='menu'),
    path('', login, name='login'),
    path('menuC/', menuClient, name='menuClients'),
    path('rClient/', read_client, name='read_client'),
    path('menuV/', menuVendas, name='menuVendas'),
    path('rSale/', read_sale, name='read_sale' ),
    path('menuL/', menuLivro, name='menuLivro'),
    path('bookList/', list_books, name='livros'),
    path('deleteB/<int:pk>', delete_book, name='delete_book'),
    path('readB/', read_book, name='read_book'),
    path('menuCm/', menuCupom, name="menuCupom"),
    path('readC/', read_cupom, name="read_cupom"),
    path('cupons/', list_cupom, name="cupons"),
    path('menuF/', menuFunc, name="menuFunc"),
    path('rFunc/', read_func, name='read_func'),
    path('deleteF/<int:pk>', delete_func, name='deleteF')

]