from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Book(models.Model):
    title = models.CharField("Book Title", max_length=255)
    author = models.CharField("Book Author", max_length=255)
    image = models.ImageField("Image", upload_to="books/images", null=True, blank=True)
    publish_date = models.DateField("Publish Date")
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    created_by = models.ForeignKey(
        User,
        related_name="user_books",
        verbose_name="Created By",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:book_detail", args=[self.pk])
