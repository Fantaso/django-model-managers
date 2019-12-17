from django.db import models

from django.db.models import Sum, Count


class AuthorQuerySet(models.QuerySet):

    def annotate_with_copies_sold(self):
        return self.annotate(copies_sold=Sum('books__copies_sold'))

    # Extra methods - Test purpose only
    def annotate_with_num_of_books(self):
        return self.annotate(num_of_books=Count('books'))

    def high_ranking_authors(self):
        """Ranking based on copies sold. Concatenating another query method."""
        return (
            self.annotate_with_copies_sold()
                .filter(copies_sold__gte=100)
        )


#############################################################################################
###### We could also only used the AuthorQuerySet.as_manager() to avoid the Manager declaration ###
#############################################################################################
# class AuthorManager(models.Manager):
#     def get_queryset(self):
#         return AuthorQuerySet(self.model, using=self._db)
#
#     def annotate_with_copies_sold(self):
#         return self.get_queryset().annotate_with_copies_sold()
#
#     # Extra methods - Test purpose only
#     def annotate_with_num_of_books(self):
#         return self.get_queryset().annotate_with_num_of_books()
#
#     def high_ranking_authors(self):
#         return self.get_queryset().high_ranking_authors()


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # objects = AuthorManager.manager()
    objects = AuthorQuerySet.as_manager()

    def __str__(self):
        return f'<Author: {self.first_name} {self.last_name}>'


class Book(models.Model):
    title = models.CharField(max_length=100)
    copies_sold = models.PositiveIntegerField()
    author = models.ForeignKey('Author',
                               on_delete=models.CASCADE,
                               related_name='books')

    def __str__(self):
        return f'<Book: {self.title} by {self.copies_sold}>'
