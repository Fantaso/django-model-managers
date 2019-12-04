from django.contrib import admin
from django.urls import path

from author_book.views import AuthorWithCopiesSoldView, AuthorMoreComplexView

urlpatterns = [
    path('admin/', admin.site.urls),

    # annotate_with_copies_sold
    path('author-list/', AuthorWithCopiesSoldView.as_view()),
    # combining more methods for a more complex queryset
    path('author-list-complex/', AuthorMoreComplexView.as_view()),
]
