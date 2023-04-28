from django.urls import path

from . import views

app_name = "tiny_urls"

urlpatterns = [
    path("shorten/", views.CreateLinkShortcutAPIView.as_view(), name="shorten"),
    path(
        "reverse/",
        views.ReverseShortenedLinkAPIView.as_view(),
        name="reverse",
    ),
    path("<slug:shortcut>", views.SlugRedirect.as_view(), name="redirect"),
]
