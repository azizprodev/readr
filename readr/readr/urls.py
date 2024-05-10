from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("books/", include("book.urls")),
    path("authors/", include("author.urls")),
]
