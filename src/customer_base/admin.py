from django.contrib import admin
from customer_base.models import Client


class Clients(admin.ModelAdmin):
    """Displaying clients class on django admin"""
    list_display = ('id', 'name', 'cpf', 'birth_date')
    search_fields = ('name', 'cpf',)
    ordering = ('name',)


admin.site.register(Client, Clients)
