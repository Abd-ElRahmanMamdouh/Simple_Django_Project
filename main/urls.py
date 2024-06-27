from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.home, name="home"),
    path(
        "books/",
        views.BookList.as_view(extra_context={"active": "books"}),
        name="book_list",
    ),
    path(
        "<int:pk>/",
        views.BookDetail.as_view(extra_context={"active": "books"}),
        name="book_detail",
    ),
    path(
        "create/",
        views.BookCreate.as_view(extra_context={"active": "books"}),
        name="book_create",
    ),
    path(
        "update/<int:pk>/",
        views.BookUpdate.as_view(extra_context={"active": "books"}),
        name="book_update",
    ),
    path(
        "delete/<int:pk>/",
        views.BookDelete.as_view(extra_context={"active": "books"}),
        name="book_delete",
    ),
    path("numbers/", views.dynamic_url_parameter, name="dynamic_url_parameter"),
]
