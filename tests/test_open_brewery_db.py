import pytest
import requests


@pytest.mark.parametrize('breweries_id', [9094, 11968, 14677, 13018, 10217])
def test_api_get_brewery_by_id(base_url_brewery_api, breweries_id):
    """Check GET BREWERIES BY ID api"""
    url = f'{base_url_brewery_api}/breweries/{breweries_id}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    assert res_json['id'] == breweries_id


@pytest.mark.parametrize('query', ['Dog', 'Epidemic', 'Brewing'])
def test_api_autocomplete(base_url_brewery_api, query):
    """Check GET AUTOCOMPLETE api"""
    url = f'{base_url_brewery_api}/breweries/autocomplete?query={query}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    for item in range(len(res_json)):
        assert 'id' in res_json[item], "no id"
        assert query in res_json[item]["name"], "query in not in name"


def test_api_404_get_brewery(base_url_brewery_api):
    """Check 404 GET BREWERIES BY ID api"""
    breweries_id = 4675656
    url = f'{base_url_brewery_api}/breweries/{breweries_id}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 404, "Incorrect code"
    assert res_json['message'] == f"Couldn't find Brewery with 'id'={breweries_id}"


@pytest.mark.parametrize('city', ['Jackson', 'Boise'])
def test_api_breweries_by_city(base_url_brewery_api, city):
    """Check GET SEARCH api"""
    url = f'{base_url_brewery_api}/breweries/?by_city={city}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    for item in range(len(res_json)):
        assert 'id' in res_json[item], "no id"
        assert city in res_json[item]["city"], "Incorrect city"


@pytest.mark.parametrize('state', ['Idaho', 'Colorado'])
@pytest.mark.parametrize('brewery_type', ['micro', 'regional'])
def test_api_breweries_by_city(base_url_brewery_api, state, brewery_type):
    """Check GET SEARCH api"""
    url = f'{base_url_brewery_api}/breweries/?by_state={state}&by_type={brewery_type}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    for item in range(len(res_json)):
        assert 'id' in res_json[item], "no id"
        assert res_json[item]["state"] == state, "Incorrect state"
        assert res_json[item]["brewery_type"] == brewery_type, "Incorrect brewery type"
