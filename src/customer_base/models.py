from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=41, unique=True)
    birth_date = models.DateField()

    objects = models.Manager()

    def __str__(self):
        return self.name
