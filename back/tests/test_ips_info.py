from fastapi.testclient import TestClient
import pytest
import requests

from src.main import create_app

URI = 'api/statistics'
URI_IP = 'api/country/'
URI_CURRENCY_RATE = 'http://data.fixer.io/api/latest'
API_KEY_CURRENCY_RATE = '?access_key=4a13599d74c802096eab16cc8a68378a'

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return TestClient(app)

def test_not_an_ip(client):
    response = client.get(URI_IP + 'hola')
    assert response.status_code == 404

def test_ip_country_spain(client):
    response = client.get(URI_IP + '83.44.196.93')
    data = response.json()
    assert response.status_code == 200
    assert data["ip"] == '83.44.196.93'
    assert data["country"] == 'España'
    assert data["country_code"] == 'ES'
    assert data["languages"] == [{'code': 'es', 'name': 'Spanish', 'native': 'Español'}, {'code': 'eu', 'name': 'Basque', 'native': 'Euskara'}, {'code': 'ca', 'name': 'Catalan', 'native': 'Català'}, {'code': 'gl', 'name': 'Galician', 'native': 'Galego'}, {'code': 'oc', 'name': 'Occitan', 'native': 'Occitan'}]
    assert data["currency_code"] == 'EUR'
    assert data["currency_rate"] == 1
    assert data["distance"] == '10490.052121425484'
    assert data["bs_as_coord"] == [-34.61315, -58.37723]
    assert data["country_coord"] == [41.93029022216797, 2.254349946975708]

def test_ip_country_china(client):
    response = client.get(URI_IP + '120.44.196.93')
    response_currency_rate  = requests.get(URI_CURRENCY_RATE + API_KEY_CURRENCY_RATE + '&base=EUR&symbols=' + 'CNY')
    currency_rate = list(response_currency_rate.json()["rates"].values())[0]
    data = response.json()
    assert response.status_code == 200
    assert data["ip"] == '120.44.196.93'
    assert data["country"] == 'China'
    assert data["country_code"] == 'CN'
    assert data["languages"] == [{'code': 'zh', 'name': 'Chinese', 'native': '中文'}]
    assert data["currency_code"] == 'CNY'
    assert data["currency_rate"] == currency_rate
    assert data["distance"] == '19262.370637510463'
    assert data["bs_as_coord"] == [-34.61315, -58.37723]
    assert data["country_coord"] == [39.91175842285156, 116.37922668457031]
