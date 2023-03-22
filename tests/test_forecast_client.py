import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.clients.forecast_client import ForecastClient

def test_get_forecast():
    client = ForecastClient()

    forecast = client.get_forecast("New York")

    assert isinstance(forecast, dict)
    assert forecast["city"] == "New York"
    assert "forecast" in forecast
