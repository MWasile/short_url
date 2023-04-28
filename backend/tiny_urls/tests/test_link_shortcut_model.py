import pytest
from django.db import IntegrityError

from tiny_urls.models import LinkShortcut


def test_link_shortcut_model_save_to_db(db):
    instance = LinkShortcut.objects.create(
        original_link="https://www.google.com",
        shortcut="google",
    )

    shortcut_db = LinkShortcut.objects.get(pk=instance.pk)

    assert shortcut_db.original_link == "https://www.google.com"


def test_link_shortcut_model_str(link_shortcut_db):
    assert (
        str(link_shortcut_db)
        == f"{link_shortcut_db.shortcut} -> {link_shortcut_db.original_link[:10]}"
    )
