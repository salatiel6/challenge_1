![](https://img.shields.io/badge/release-v1.1.0-gold)  
![](https://img.shields.io/badge/python-v3.10.1-blue)
![](https://img.shields.io/badge/Django-v4.0.4-white)
![](https://img.shields.io/badge/mysqlclient-v2.1.0-000000)

![](https://img.shields.io/badge/passed_tests-5-brightgreen)
![](https://img.shields.io/badge/failed_tests-0-red)  
![](https://img.shields.io/badge/coverage-94%25-green)

# Customer Base Challenge

Application created on the standards of the `Django` and `django_rest_framework` frameworks, in the `python` language.  
Data administration done in `SQLite` allowing all interactions requested in the challenge.  
API allocated on `Python Anywhere` server, thus allowing external access.

---

## EndPoints

Register clients:
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

---

Search client by CPF:
> ![](https://img.shields.io/badge/method-GET-pink)  
> `url`: `http://salatiel6.pythonanywhere.com/clients/?cpf=49529035080`  (cpf always without mask)

---

List all clients with pagination:
> ![](https://img.shields.io/badge/method-GET-pink)  
> `url`: `http://salatiel6.pythonanywhere.com/clients/?page=1`

---

## How to execute by yourself
Every endpoint is working in `http://salatiel6.pythonanywhere.com/clients/`, but if you want to build and execute the server on your PC, just follow these steps.

Pre-requirements:
- [Git](https://git-scm.com/downloads)
- [Python3.10](https://www.python.org/downloads/)

1. Clone the repository    
`git clone https://github.com/salatiel6/challenge_1.git`


2. Open the challenge directory  
Widnows/Linux:`cd challenge_1`  
Mac: `open challenge_1`


3. Create virtual enviroment (recommended)  
`python -m venv ./venv`


4. Activate virtual enviroment (recommended)  
Windows: `venv\Scripts\activate`  
Linux/Mac: `source venv/bin/activate`


5. Install every dependencies  
`pip install -r requirements.txt`


6. Open the source directory  
Windows/Linux: `cd src`  
Mac: `open src`


7. Run tests  
Without coverage: `python manage.py test`  
With coverage: `coverage run manage.py test -v 2` | `coverage report`


8. Migrate every database  
`python manage.py migrate`


9. Run the server  
`python manage.py runserver`