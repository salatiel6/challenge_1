from rest_framework import viewsets, filters
from customer_base.serializers import ClientSerializer
from customer_base.models import Client
from customer_base.pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend


class ClientsViewSet(viewsets.ModelViewSet):
    """Creating visualizer for Clients"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = DefaultPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    filterset_fields = ['cpf']
