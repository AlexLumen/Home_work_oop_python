import requests


def test_url_code(base_url, status_code):
    res = requests.get(base_url)
    assert res.status_code == int(status_code), "Incorrect status code"
