# django-simple-project
_Just a simple Django project where you can save products (Name, Price, Stock and Image) in the database._

**Como executar o projeto:**

1. Instale os pacotes necessários pro projeto funcionar:
```pip
pip install -r requirements.txt
```

<br>

2. Crie o arquivo _.env_ e adicione as seguintes variáveis de ambiente:
- DEBUG = True
- ALLOWED_HOSTS = localhost,127.0.0.1
- SECRET_KEY = 'yourkey'

<br>

3. Faça as migrações necessárias pro projeto:
```sudo
python manage.py makemigrations
```
```sudo
python manage.py migrate
```

<br> 

4. Crie um super usuário:
```sudo
python manage.py createsuperuser
```
<br>

5. Rode o servidor:
```sudo
python manage.py runserver
```

<br>

6. URLs existentes no projeto:


- index: mostra todos os produtos cadastrados. http://127.0.0.1:8000/


- contact: formulário de envio de email. http://127.0.0.1:8000/contact


- product: formulário de cadastro de produto (precisa estar logado no admin do Django). http://127.0.0.1:8000/product

<br>


7. Entre no admin do projeto:
- http://127.0.0.1:8000/admin

<br>

8. Use o projeto.
