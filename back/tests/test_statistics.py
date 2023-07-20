from fastapi.testclient import TestClient
import pytest
from src.main import create_app

URI = 'api/statistics'
URI_IP = 'api/country/'

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return TestClient(app)

def test_intial_state(client):
    response = client.get(URI)
    data = response.json()
    assert response.status_code == 200
    assert data["min_distance"] == 100000000000000000
    assert data["max_distance"] == 0
    assert data["mean_distance"] == 0



def test_updated_state_one_ip_call(client):
    response_ip = client.get(URI_IP + '83.44.196.93')
    response = client.get(URI)
    data = response.json()
    assert response.status_code == 200
    assert response_ip.status_code == 200
    assert data["min_distance"] == 10490.052121425484
    assert data["max_distance"] == 10490.052121425484
    assert data["mean_distance"] == 10490.052121425484

def test_updated_state_two_ip_call(client):
    response_ip = client.get(URI_IP + '83.44.196.93')
    response_ip = client.get(URI_IP + '83.44.196.93')
    response = client.get(URI)
    data = response.json()
    assert response.status_code == 200
    assert response_ip.status_code == 200
    assert data["min_distance"] == 10490.052121425484
    assert data["max_distance"] == 10490.052121425484
    assert data["mean_distance"] == 10490.052121425484

def test_updated_state_two_different_ip_call(client):
    response_ip = client.get(URI_IP + '83.44.196.93')
    response_ip_china = client.get(URI_IP + '120.44.196.93')
    response = client.get(URI)
    data = response.json()
    assert response.status_code == 200
    assert response_ip.status_code == 200
    assert response_ip_china.status_code == 200
    assert data["min_distance"] == 10490.052121425484
    assert data["max_distance"] == 19262.370637510463
    assert data["mean_distance"] == 14876.211379467973
