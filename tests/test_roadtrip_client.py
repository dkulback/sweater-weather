import os
import pytest
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.clients.roadtrip_client import RoadtripClient

@pytest.fixture(scope='module')
def roadtrip_client():
    return RoadtripClient()

def test_get_roadtrip_success(roadtrip_client):
    response = roadtrip_client.get_roadtrip('Denver,CO', 'Pueblo,CO')

    assert 'route' in response
    assert 'formattedTime' in response['route']
    assert 'locations' in response['route']
    assert isinstance(response['route']['locations'], list)
    assert 'adminArea5' in response['route']['locations'][0]
    assert 'adminArea5' in response['route']['locations'][1]
    assert response['route']['locations'][0]['adminArea5'] == 'Denver'
    assert response['route']['locations'][1]['adminArea5'] == 'Pueblo'

