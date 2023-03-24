import os
import requests
import pdb
from dotenv import load_dotenv


class GeocoderClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("MAP_API_KEY")
        self.base_url = "http://www.mapquestapi.com/geocoding/v1/address"
    def get_coordinates(self, city):
        params = {
            'key': self.api_key,
            'location': city,
            'maxResults': 1
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve coordinates for {city}. Status code: {response.status_code}")

        coordinates = response.json()

        return coordinates
