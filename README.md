![](https://img.shields.io/badge/release-v1.0.0-gold)  
![](https://img.shields.io/badge/python-v3.10.1-blue)
![](https://img.shields.io/badge/Django-v4.0.4-white)
![](https://img.shields.io/badge/mysqlclient-v2.1.0-000000)

![](https://img.shields.io/badge/passed_tests-5-brightgreen)
![](https://img.shields.io/badge/failed_tests-0-red)  
![](https://img.shields.io/badge/coverage-94%25-green)

<h1><p align="center">Customer Base Challenge</p></h1>

Aplicação criada sobre os padrões dos frameworks `Django` e `django_rest_framework`, na liguagem `python`.  
Administração de dados feita no `SQLite` possibilitando todas as interações pedidas no desafio.  
API alocada em servidor da `Python Anywhere`, permitindo assim acessos externos.

<h2><p align="center">EndPoints</p></h2>

Cadastrar Clientes:
> ![](https://img.shields.io/badge/method-POST-purple)  
> `url`: `http://salatiel6.pythonanywhere.com/clients/`  
>
> `body example`:
> ```
> {
>     "name": "Client Name",
>     "cpf": "495.290.350-80",
>     "birth_date": "1975-02-11"
> }
> ```

Buscar cliente por CPF:
> ![](https://img.shields.io/badge/method-GET-pink)  
> `url`: `http://salatiel6.pythonanywhere.com/clients/?cpf=49529035080`  (cpf sempre sem máscara)

Listar todos os clientes:
> ![](https://img.shields.io/badge/method-GET-pink)  
> `url`: `http://salatiel6.pythonanywhere.com/clients/?page=1`