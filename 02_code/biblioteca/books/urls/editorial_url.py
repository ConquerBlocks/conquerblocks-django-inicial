from django.urls import path

from books.views import (
  EditorialListView,
  EditorialDetailView,
  EditorialCreateView,
  EditorialUpdateView,
  EditorialDeleteView
)

app_name = "editorial"

urlpatterns = [
    path("list/", EditorialListView.as_view(), name="list"),
    path("detail/<pk>/", EditorialDetailView.as_view(), name="detail"),
    path("create/", EditorialCreateView.as_view(), name="create"),
    path("update/<pk>", EditorialUpdateView.as_view(), name="update"),
    path("delete/<pk>", EditorialDeleteView.as_view(), name="delete"),
]
