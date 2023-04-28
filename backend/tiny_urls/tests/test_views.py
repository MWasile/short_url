def test_create_link_shortcut_api_view(api_client, db):
    response = api_client.post(
        "/api/v1/shorten/",
        data={"original_link": "https://www.google.com"},
        format="json",
    )

    assert response.status_code == 201


def test_create_link_shortcut_api_view_invalid(api_client, db):
    response = api_client.post(
        "/api/v1/shorten/",
        data={"original_link": "google.com"},
        format="json",
    )

    assert response.status_code == 400


def test_create_link_shortcut_api_view_existed(api_client, link_shortcut_db):
    response = api_client.post(
        "/api/v1/shorten/",
        data={"original_link": "https://www.google.com"},
        format="json",
    )

    assert response.status_code == 200
