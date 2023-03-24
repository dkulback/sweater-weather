import os
import requests
from dotenv import load_dotenv

class ForecastClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/onecall"

    def get_forecast(self, lat, lng):
        params = {
            'appid': self.api_key,
            'units': 'imperial',
            'exclude': 'minutely',
            'lat': lat,
            'lon': lng
        }

        response = requests.get(self.base_url, params = params)
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve forecast for {lat}, {lng}. Status code: {response.status_code}")

        forecast = response.json()

        return forecast
