from typing import Any
from urllib.parse import urlparse

from django.views.generic import RedirectView
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from . import serializers
from . import models


class CreateLinkShortcutAPIView(CreateAPIView):
    """
    View for creating a new link shortcut.
    Method: POST
    Body: {"original_link": "https://www.google.com/"}
    Response: {"original_link": "https://www.google.com/", "shortcut": "googlecom-5f3a1"}
    """

    serializer_class = serializers.LinkShortcutSerializer

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        catch_existed = models.LinkShortcut.objects.filter(
            original_link=serializer.validated_data["original_link"]
        ).first()

        if catch_existed:
            return Response(
                self.get_serializer(catch_existed).data, status=status.HTTP_200_OK
            )

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReverseShortenedLinkAPIView(APIView):
    """
    View for getting the original link from the shortcut.
    Method: POST
    Body: {"shortcut": "googlecom-5f3a1"}
    Response: {"shortcut": "googlecom-5f3a1", "original_link": "https://www.google.com/"}
    """

    @staticmethod
    def post(request):
        serializer = serializers.ShortenedLinkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        slug = urlparse(serializer.validated_data["shortcut"]).path.replace("/", "")
        link_shortcut = get_object_or_404(models.LinkShortcut, shortcut=slug)

        return Response(
            serializers.ShortenedLinkSerializer(link_shortcut).data,
            status=status.HTTP_200_OK,
        )


class SlugRedirect(RedirectView):
    """
    Redirects to the original link.
    """

    permanent = False
    query_string = True

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str:
        try:
            return models.LinkShortcut.objects.get(
                shortcut=kwargs["shortcut"]
            ).original_link
        except models.LinkShortcut.DoesNotExist:
            return reverse("shorten")
