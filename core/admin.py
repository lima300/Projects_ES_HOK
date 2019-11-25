from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Book)
admin.site.register(Sale)
admin.site.register(Cupom)


