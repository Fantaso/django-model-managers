from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from author_book.views import AuthorWithCopiesSoldView, AuthorMoreComplexView

urlpatterns = [
    path('admin/', admin.site.urls),

    # annotate_with_copies_sold
    path('author-list/', AuthorWithCopiesSoldView.as_view()),
    # combining more methods for a more complex queryset
    path('author-list-complex/', AuthorMoreComplexView.as_view()),
]

# Adding debug toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
