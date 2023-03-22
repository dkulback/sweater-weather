import os
import requests
import pdb
from dotenv import load_dotenv

load_dotenv()

class ForecastClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/forecast"

    def get_forecast(self, city):
        url = f"{self.base_url}?q={city}&appid={self.api_key}"

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Failed to retrieve forecast data for {city}. Status code: {response.status_code}")

        forecast_data = response.json()

        forecast = {"city": forecast_data["city"]["name"], "forecast": []}

        for item in forecast_data["list"]:
            forecast["forecast"].append({"date": item["dt_txt"], "description": item["weather"][0]["description"]})

        return forecast
