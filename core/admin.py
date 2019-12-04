from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Book)
admin.site.register(Sale)
admin.site.register(Cupom)
admin.site.register(Employee)

admin.site.unregister(Group)



