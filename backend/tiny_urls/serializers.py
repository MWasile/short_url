from django.urls import reverse
from rest_framework import serializers

from . import models


class LinkShortcutSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new link shortcut.
    """

    shortcut_url = serializers.SerializerMethodField()

    class Meta:
        model = models.LinkShortcut
        fields = ("original_link", "shortcut_url")
        read_only_fields = ("shortcut_url",)

    def get_shortcut_url(self, obj):
        return self.context["request"].build_absolute_uri(
            reverse("tiny_urls:redirect", args=[obj.shortcut])
        )


class ShortenedLinkSerializer(serializers.Serializer):
    """
    Serializer for getting the original link from the shortcut.
    """

    shortcut = serializers.URLField()
    original_link = serializers.URLField(read_only=True)

    class Meta:
        fields = ("shortcut", "original_link")
