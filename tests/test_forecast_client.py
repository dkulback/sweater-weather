import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.clients.forecast_client import ForecastClient

def test_get_forecast():
    client = ForecastClient()

    forecast = client.get_forecast(40.730610, -73.935242)

    assert isinstance(forecast, dict)
    assert "current" in forecast
    assert "temp" in forecast["current"]
    assert "feels_like" in forecast["current"]
    assert "weather" in forecast["current"]
    assert "description" in forecast["current"]["weather"][0]
    assert "daily" in forecast
    assert "temp" in forecast["daily"][0]
    assert "min" in forecast["daily"][0]["temp"]
    assert "max" in forecast["daily"][0]["temp"]
    assert "weather" in forecast["daily"][0]


