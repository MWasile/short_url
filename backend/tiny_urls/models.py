from django.db import models
from django.db.models import URLField, CharField


class LinkShortcut(models.Model):
    """
    Link shortcut model. Stores the original link and the shortcut.

    Attributes:
        original_link (str): Original link.
        shortcut (str): Shortcut.
    """

    original_link: URLField = models.URLField()
    shortcut: CharField = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.shortcut} -> {self.original_link[:10]}"

    class Meta:
        verbose_name_plural = "Link shortcuts"
