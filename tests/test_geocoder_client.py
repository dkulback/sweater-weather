import os
import pytest
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.clients.geocoder_client import GeocoderClient

@pytest.fixture(scope="module")
def geocoder_client():
    return GeocoderClient()

def test_get_coordinates_success(geocoder_client):
    # Ensure that get_coordinates() returns coordinates for New York City
    city = "New York City"
    response = geocoder_client.get_coordinates(city)
    assert response["results"][0]["providedLocation"]["location"] == city
    assert "latLng" in response["results"][0]["locations"][0]
    assert "lat" in response["results"][0]["locations"][0]["latLng"]
    assert "lng" in response["results"][0]["locations"][0]["latLng"]
