<!-- logo -->
<a href="https://github.io/fantaso">
<img src="/readme/fantaso.png" align="right" />
</a>

<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  Django Model Managers App
</h1>

> Web app to test case Managers for models in Django. The App consists in listing on html page (http://localhost:8000/author-list/) all the Authors with the sum of copies sold of all their books.

<!-- build -->
<!-- [![Build Status][travis-image]][travis-link] -->




Test case allows the user to visit website to view a list of all authors and their amount of books sold per author.

It is partly tested as only and was developed as showcase only.




How Django Models Managers Works:
- You can open the browser with the url http://localhost:8000/author-list to view the list of authors and all book's copies sold.
- You can open the browser with the url http://localhost:8000/author-list-complex to view the list of authors and all book's copies sold and number of books and only the authors who have sold more than 100 books.


<br><br>

## Index:
- #### Installation
    1. Installing Django Models Managers App
    2. Instructions to test with django-debug-toolbar

- #### Usage:
    1. Available Endpoints
    2. Tests INFO

- #### Information:
- #### Maintainer


<br><br>


## Installation:
#### 1.Installing Django Models Managers App

1. Clone repository and go inside the repository folder "django-model-managers"
```sh
git clone https://github.com/Fantaso/django-model-managers.git
```

2. Create your virtualenv and install the packages
```sh
pip install -r requirements.txt
```

3. Migrate the database.
```sh
python manage.py makemigrations && python manage.py migrate
```

4. Run the application.
```sh
python manage.py runserver
```


#### 2.Instructions to test with django-debug-toolbar

1. Create a superuser in order to access the Django Admin app and follow the instructions
```sh
python manage.py createsuperuser
```

2. Go to http://localhost:8000/admin and login with your username and password created in the previous step


3. Once in the Admin app, add as many Authors and Books to your database.


4. Once you have added all authors and books go to the endpoints available and you should see a webpage with a list of all Authors and Book information rendered with the django Debug Toolbar on the side. Just click the logo "DjDT" on the right side of the website and check it.


<br>

## USAGE
#### 1. Endpoint List
URI Example: `http://localhost:8000/author-list`

URI Example: `http://localhost:8000/author-list-complex`


<br>


#### 2. Tests INFO
A small TestCase was done to check the manager annotate_with_copies_sold query method since, to tested over the webapp template at eh endpoint of 'author-list/' or 'author-list-complex/' will need extra requirements like migrating, creating a superuser and adding on the admin panel new Authors and Books to the local database

1. Run the Django Models Managers app tests locally with:
```sh
python manage.py test
```

<br>





## Information:
| Technology Stack |  |  |
| :- | :-: | :- |
| Python                    | ![back-end][python]                   | Back-End |
| Django                    | ![django][django]                     | Web Framework |
| Django Debug toolbar      | ![django-debug-toolbar][django-debug-toolbar] | Browser Debug Tool |

<br><br>


## Maintainer
Get in touch -–> [Github][github-profile]



<!-- Links -->
<!-- Profiles -->
[github-profile]: https://github.com/fantaso/
[linkedin-profile]: https://www.linkedin.com/
[fantaso]: https://www.fantaso.de/
<!-- Extra -->


<!-- Repos -->
[github-repo]: https://github.com/Fantaso/django-model-managers

<!-- Builds -->
[travis-link]: https://travis-ci.org/
[travis-image]: https://travis-ci.org/

<!-- images -->
[python]: readme/python.png
[django]: readme/django.png
[django-debug-toolbar]: readme/django-debug-toolbar.png