import pytest
from weather_insights.data_fetcher import fetch_weather_data
from weather_insights.exceptions import WeatherDataError

def test_fetch_weather_data_success(mock_requests):
    # Mock successful API response
    pass

def test_fetch_weather_data_failure(mock_requests):
    # Mock failure case
    pass