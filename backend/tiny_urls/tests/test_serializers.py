from tiny_urls.models import LinkShortcut
from tiny_urls.serializers import LinkShortcutSerializer


def test_link_shortcut_serializer_deserialization():
    serializer = LinkShortcutSerializer(
        data={"original_link": "https://www.google.com/"}
    )

    assert serializer.is_valid() is True
    assert serializer.validated_data == {
        "original_link": "https://www.google.com/",
    }


def test_link_shortcut_serializer_deserialization_invalid():
    serializer = LinkShortcutSerializer(data={"original_link": "google.com"})

    assert serializer.is_valid() is False
    assert serializer.errors == {
        "original_link": ["Enter a valid URL."],
    }
