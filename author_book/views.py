from django.views.generic import ListView

from author_book.models import Author


# To test case the manager 2 views are created using the same template
# 1 - To test only the method annotate_with_copies_sold()
# 2 - To test a more complex queryset combining diff manager methods

class AuthorWithCopiesSoldView(ListView):
    template_name = 'author_book/author_list.html'
    context_object_name = 'authors'
    queryset = Author.objects.annotate_with_copies_sold()


class AuthorMoreComplexView(ListView):
    template_name = 'author_book/author_list.html'
    context_object_name = 'authors'

    queryset = (
        Author.objects
            .high_ranking_authors()
            .annotate_with_copies_sold()
            .annotate_with_num_of_books()
            .order_by('-copies_sold')
    )
