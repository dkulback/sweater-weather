import pytest
import json
from app import create_app


@pytest.fixture(scope='session')
def api_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


def test_get_forecast(api_client):
    url = '/api/v1/forecast?location=denver,co'
    headers = {"Content-Type": 'application/json',
               "Accept": 'application/json'}

    # Test valid params
    response = api_client.get(url, headers=headers)
    assert response.status_code == 200
    forecast = json.loads(response.data.decode('utf-8'))

    current_weather = forecast['data']['attributes']['current_weather']
    daily = forecast['data']['attributes']['daily_weather'][0]
    hourly = forecast['data']['attributes']['hourly_weather'][0]

    assert isinstance(forecast, dict)
    assert 'data' in forecast
    assert isinstance(forecast['data'], dict)
    assert 'id' in forecast['data'] and forecast['data']['id'] is None
    assert 'type' in forecast['data'] and isinstance(
        forecast['data']['type'], str)
    assert 'attributes' in forecast['data'] and isinstance(
        forecast['data']['attributes'], dict)

    assert isinstance(current_weather, dict)
    assert 'temperature' in current_weather
    assert 'sunrise' in current_weather
    assert 'datetime' in current_weather
    assert 'sunset' in current_weather
    assert 'feels_like' in current_weather
    assert 'humidity' in current_weather
    assert 'uvi' in current_weather
    assert 'visibility' in current_weather
    assert 'conditions' in current_weather
    assert 'icon' in current_weather

    assert 'daily_weather' in forecast['data']['attributes']
    assert isinstance(forecast['data']['attributes']['daily_weather'], list)
    assert len(forecast['data']['attributes']['daily_weather']) == 5
    assert 'datetime' in daily and isinstance(daily['datetime'], str)
    assert 'sunrise' in daily and isinstance(daily['sunrise'], str)
    assert 'sunset' in daily and isinstance(daily['sunset'], str)
    assert 'max_temp' in daily and isinstance(daily['max_temp'], float)
    assert 'min_temp' in daily and isinstance(daily['min_temp'], float)
    assert 'conditions' in daily and isinstance(daily['conditions'], str)
    assert 'icon' in daily and isinstance(daily['icon'], str)

    assert 'hourly_weather' in forecast['data']['attributes']
    assert isinstance(forecast['data']['attributes']['hourly_weather'], list)
    assert len(forecast['data']['attributes']['hourly_weather']) == 48
    assert 'time' in hourly and isinstance(hourly['time'], str)
    assert 'temperature' in hourly and isinstance(hourly['temperature'], float)
    assert 'conditions' in hourly and isinstance(hourly['conditions'], str)
    assert 'icon' in hourly and isinstance(hourly['icon'], str)

    assert 'pressure' not in current_weather
    assert 'dewpoint' not in current_weather
    assert 'wind_speed' not in current_weather
    assert 'wind_deg' not in current_weather

    assert 'pressure' not in daily
    assert 'dewpoint' not in daily
    assert 'wind_speed' not in daily
    assert 'wind_deg' not in daily

    assert 'pressure' not in hourly
    assert 'dewpoint' not in hourly
    assert 'wind_speed' not in hourly
