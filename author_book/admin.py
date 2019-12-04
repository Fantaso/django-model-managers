from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
=======
from author_book.models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'copies_sold', 'author']
>>>>>>> tmp
