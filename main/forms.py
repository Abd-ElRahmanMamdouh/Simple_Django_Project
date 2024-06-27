from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("created_by",)
        widgets = {
            "publish_date": forms.DateInput(attrs={"type": "date"}),
        }
