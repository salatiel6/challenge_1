import customer_base.validators as validate
import re

from customer_base.models import Client
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def validate(self, data):
        validate.cpf_format(data['cpf'])
        validate.cpf_number(data['cpf'])

        data['cpf'] = re.sub(r'\W', '', data['cpf'])
        return data
