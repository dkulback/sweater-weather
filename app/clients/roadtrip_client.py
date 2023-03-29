import os
import requests
import pdb
from dotenv import load_dotenv


class RoadtripClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("MAP_API_KEY")
        self.base_url = "http://www.mapquestapi.com/directions/v2/route"

    def get_roadtrip(self, origin, destination):
        query_params = {
            "key": self.api_key,
            "from": origin,
            "to": destination
        }
        response = requests.get(self.base_url, params=query_params)

        return response.json()
