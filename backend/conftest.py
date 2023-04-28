import pytest


@pytest.fixture
def link_shortcut_db(db):
    from tiny_urls.models import LinkShortcut

    return LinkShortcut.objects.create(
        original_link="https://www.google.com",
        shortcut="google",
    )
