from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .forms import BookForm
from .models import Book


def home(request):
    return render(request, "home.html", {"active": "home"})


class BookCreate(SuccessMessageMixin, CreateView):
    model = Book
    template_name = "base/forms/create_update.html"
    success_url = reverse_lazy("main:book_list")
    success_message = "Book successfully created"
    form_class = BookForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            user = self.request.user
            form.instance.created_by = user
            form.save()
        return super().form_valid(form)


class BookUpdate(SuccessMessageMixin, UpdateView):
    model = Book
    template_name = "base/forms/create_update.html"
    success_url = reverse_lazy("main:book_list")
    success_message = "Book successfully updated"
    form_class = BookForm


class BookDelete(SuccessMessageMixin, DeleteView):
    model = Book
    template_name = "base/forms/delete.html"
    success_url = reverse_lazy("main:book_list")
    success_message = "Book successfully deleted"


class BookList(ListView):
    model = Book
    template_name = "main/list.html"
    context_object_name = "books"
    paginate_by = 2


class BookDetail(DetailView):
    model = Book
    template_name = "main/detail.html"
    context_object_name = "book"


def multiplication_table(number, limit=10):
    table = []
    for i in range(1, limit + 1):
        table.append(f"{number} x {i} = {number * i}")
    return table


def dynamic_url_parameter(request):
    number = request.GET.get("number")
    if number.isdigit():
        multi_table = multiplication_table(int(number))
    else:
        multi_table = None
    context = {"multi_table": multi_table, "number": number}
    return render(request, "main/dynamic_parameter.html", context)
