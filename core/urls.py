from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('book/', save_book, name='save_book'),
    path('client/', save_client, name='save_client'),
    path('updateC/<int:pk>/', update_client, name='update_client'),
    path('deleteC/<int:pk>/', delete_client, name='delete_client'),
    path('',list_client, name='client_list'),
]