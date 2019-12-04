from django.test import TestCase

from author_book.models import Author, Book


class AuthorModelTests(TestCase):
    def setUp(self):
        # Authors
        carlos_data = dict(first_name='Carlos', last_name='Rosas')
        maria_data = dict(first_name='Maria', last_name='Mueller')
        juanita_data = dict(first_name='Juanita', last_name='Del Carmen')

        # Books
        carlos_book_one_data = dict(title='Vida Larga', copies_sold=80)
        carlos_book_two_data = dict(title='Vida Corta', copies_sold=25)
        maria_book_one_data = dict(title='Leben ist lang', copies_sold=205)
        juanita_book_one_data = dict(title='Life has no time', copies_sold=90)

        # Authors model creation
        carlos = Author.objects.create(**carlos_data)
        maria = Author.objects.create(**maria_data)
        juanita = Author.objects.create(**juanita_data)

        # Books model creation
        Book.objects.create(author=carlos, **carlos_book_one_data)
        Book.objects.create(author=carlos, **carlos_book_two_data)
        Book.objects.create(author=maria, **maria_book_one_data)
        Book.objects.create(author=juanita, **juanita_book_one_data)

    def test_annotation_with_copies_sold(self):
        # Test first author
        first_author = Author.objects.annotate_with_copies_sold().first()
        self.assertEqual(first_author.copies_sold, 105)
        self.assertEqual(first_author.first_name, 'Carlos')

        # Test a concatenation of query before using the manager method
        carlos = Author.objects.filter(first_name='Carlos').annotate_with_copies_sold().first()

        self.assertEqual(carlos.copies_sold, 105)
        self.assertEqual(carlos.first_name, 'Carlos')
