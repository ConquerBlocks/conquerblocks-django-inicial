from django.urls import path

from books.views import (
  LibrosListView,
  LibroDetailView
)

app_name = "libro"

urlpatterns = [
    path("list/", LibrosListView.as_view(), name="list"),
    path("detail/<pk>/", LibroDetailView.as_view(), name="detail"),
]
