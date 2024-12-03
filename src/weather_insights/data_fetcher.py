import requests
from .exceptions import WeatherDataError

def fetch_weather_data(city: str, api_key: str) -> dict:
    """Fetch weather data for a given city using OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise WeatherDataError(f"Failed to fetch data: {response.json().get('message')}")
    
    return response.json()