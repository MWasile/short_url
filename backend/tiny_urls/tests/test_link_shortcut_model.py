from tiny_urls.models import LinkShortcut


def test_link_shortcut_model_save_to_db(db):
    instance = LinkShortcut.objects.create(
        original_link="https://www.google.com",
        shortcut="google",
    )

    shortcut_db = LinkShortcut.objects.get(pk=instance.pk)

    assert shortcut_db.original_link == "https://www.google.com"
