from urllib.parse import urlparse
from uuid import uuid4

from django.db import models
from django.db.models import URLField, CharField, SlugField
from django.utils.text import slugify


class LinkShortcut(models.Model):
    """
    Link shortcut model. Stores the original link and the shortcut.

    Attributes:
        original_link (str): Original link.
        shortcut (str): Shortcut, automatically generated.
    """

    original_link: URLField = models.URLField()
    shortcut: SlugField = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.shortcut} -> {self.original_link[:10]}"

    def save(self, *args, **kwargs) -> None:
        """
        Generates unique shortcut before saving.
        """

        url_info = urlparse(str(self.original_link)).netloc

        self.shortcut = slugify(f"{url_info}-{uuid4().hex[:5]}")

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Link shortcuts"
