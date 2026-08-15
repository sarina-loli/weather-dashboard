"""
services.py

WHY: Keeping all external-API logic in one "service layer" file (instead
of inside views.py) means:
- views.py stays thin and only handles HTTP request/response concerns.
- If we ever swap OpenWeatherMap for another provider, we only change
  this one file.
- It's easy to unit test this logic in isolation.

This module calls the OpenWeatherMap "Current Weather" and "5 Day / 3
Hour Forecast" endpoints, then reshapes their JSON into the exact shape
our React frontend expects.
"""

from datetime import datetime, timezone, timedelta
import requests
from django.conf import settings

BASE_URL = 'https://api.openweathermap.org/data/2.5'


class CityNotFoundError(Exception):
    """Raised when OpenWeatherMap can't find the requested city."""
    pass


class WeatherServiceError(Exception):
    """Raised for any other upstream API failure (bad key, network, etc.)."""
    pass


def _get(url, params):
    try:
        response = requests.get(url, params=params, timeout=8)
    except requests.RequestException as exc:
        raise WeatherServiceError(f'Could not reach weather provider: {exc}')

    if response.status_code == 404:
        raise CityNotFoundError('City not found.')

    if response.status_code == 401:
        raise WeatherServiceError(
            'Invalid or missing OpenWeatherMap API key. Check your .env file.'
        )

    if response.status_code != 200:
        raise WeatherServiceError(
            f'Weather provider returned an unexpected error (status {response.status_code}).'
        )

    return response.json()


def _local_time(unix_dt, tz_offset_seconds):
    """Convert a UTC unix timestamp + timezone offset (seconds) into a
    human-readable local time string for the searched city."""
    local_dt = datetime.utcfromtimestamp(unix_dt) + timedelta(seconds=tz_offset_seconds)
    return local_dt.strftime('%Y-%m-%d %H:%M')


def _time_only(unix_dt, tz_offset_seconds):
    local_dt = datetime.utcfromtimestamp(unix_dt) + timedelta(seconds=tz_offset_seconds)
    return local_dt.strftime('%H:%M')


def get_current_weather(city):
    """Fetch and reshape current weather data for a city."""
    params = {
        'q': city,
        'appid': settings.OPENWEATHER_API_KEY,
        'units': 'metric',
    }
    data = _get(f'{BASE_URL}/weather', params)

    tz_offset = data.get('timezone', 0)

    return {
        'city': data['name'],
        'country': data['sys']['country'],
        'temperature': round(data['main']['temp']),
        'feels_like': round(data['main']['feels_like']),
        'description': data['weather'][0]['description'].title(),
        'icon': data['weather'][0]['icon'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'pressure': data['main']['pressure'],
        'visibility': round(data.get('visibility', 0) / 1000, 1),  # metres -> km
        'sunrise': _time_only(data['sys']['sunrise'], tz_offset),
        'sunset': _time_only(data['sys']['sunset'], tz_offset),
        'local_time': _local_time(data['dt'], tz_offset),
        'timezone_offset': tz_offset,
        'coord': data['coord'],
    }


def get_forecast(city):
    """Fetch the 5 day / 3 hour forecast and split it into:
    - hourly: the next 24 hours (8 entries of 3-hour steps)
    - daily: one summary entry per day for the next 5 days
    """
    params = {
        'q': city,
        'appid': settings.OPENWEATHER_API_KEY,
        'units': 'metric',
    }
    data = _get(f'{BASE_URL}/forecast', params)
    tz_offset = data['city']['timezone']
    entries = data['list']

    hourly = []
    for entry in entries[:8]:
        hourly.append({
            'time': _time_only(entry['dt'], tz_offset),
            'temperature': round(entry['main']['temp']),
            'icon': entry['weather'][0]['icon'],
            'description': entry['weather'][0]['description'].title(),
        })

    # Group 3-hour entries by calendar day (local time) to build a
    # simple 5-day forecast: min/max temp + the midday icon/description.
    days = {}
    for entry in entries:
        local_dt = datetime.utcfromtimestamp(entry['dt']) + timedelta(seconds=tz_offset)
        day_key = local_dt.strftime('%Y-%m-%d')
        days.setdefault(day_key, []).append((local_dt.hour, entry))

    daily = []
    for day_key, hour_entries in list(days.items())[:5]:
        temps = [e['main']['temp'] for _, e in hour_entries]
        # Prefer the entry closest to midday for the representative icon.
        _, midday_entry = min(hour_entries, key=lambda h: abs(h[0] - 12))
        day_date = datetime.strptime(day_key, '%Y-%m-%d')
        daily.append({
            'date': day_key,
            'day_name': day_date.strftime('%A'),
            'temp_min': round(min(temps)),
            'temp_max': round(max(temps)),
            'icon': midday_entry['weather'][0]['icon'],
            'description': midday_entry['weather'][0]['description'].title(),
        })

    return {'hourly': hourly, 'daily': daily}


def get_weather_data(city):
    """Combine current weather + forecast into one payload for the API."""
    current = get_current_weather(city)
    forecast = get_forecast(city)
    return {
        'current': current,
        'hourly_forecast': forecast['hourly'],
        'daily_forecast': forecast['daily'],
    }
