from django.urls import path

from books.views import (
  LibrosListView,
)

app_name = "libro"

urlpatterns = [
    path("list/", LibrosListView.as_view(), name="list"),
]
