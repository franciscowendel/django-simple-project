# Django Simple Project
*A simple Django project* where user can save products (Name, Price, Stock and Image) in the database; API of products included.

**How execute the project:**

1. Install all dependencies for the project to work:
```pip
pip install -r requirements.txt
```

<br>

2. Create the file **.env** and the variables below:
- DEBUG = True
- ALLOWED_HOSTS = localhost,127.0.0.1
- SECRET_KEY = 'yourkey'

<br>

3. Make the necessary migrations for the project:
```sudo
python manage.py makemigrations
```
```sudo
python manage.py migrate
```

<br> 

4. Create a superuser:
```sudo
python manage.py createsuperuser
```
<br>

5. Run the server:
```sudo
python manage.py runserver
```

<br>

6. Login to the admin:
- http://127.0.0.1:8000/admin


<br>

7. URLs of the project:


- index: show all the registered products. http://127.0.0.1:8000/


- contact: email submission form. http://127.0.0.1:8000/contact


- product: product registration form (you need to be logged in!). http://127.0.0.1:8000/product_registration

- API of all products: http://127.0.0.1:8000/api/v2/products/
- API of one especific product: http://127.0.0.1:8000/api/v2/products/1


<br>


8. Use the project!
