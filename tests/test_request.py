import requests


def test_request_is_successful():
    response = requests.get("https://google.com")
    assert response.status_code == 200

