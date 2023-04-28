from django.urls import reverse
from rest_framework import serializers

from . import models


class LinkShortcutSerializer(serializers.ModelSerializer):
    shortcut_url = serializers.SerializerMethodField()

    class Meta:
        model = models.LinkShortcut
        fields = ("original_link", "shortcut", "shortcut_url")
        read_only_fields = ("shortcut",)

    def get_shortcut_url(self, obj):
        return self.context["request"].build_absolute_uri(
            reverse("tiny_urls:redirect", args=[obj.shortcut])
        )
