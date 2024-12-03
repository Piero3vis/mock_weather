from weather_insights.analyzer import WeatherAnalyzer

def test_get_temperature_celsius():
    weather_data = {"main": {"temp": 300}}
    analyzer = WeatherAnalyzer(weather_data)
    assert abs(analyzer.get_temperature_celsius() - 26.85) < 0.01

def test_get_weather_description():
    weather_data = {"weather": [{"description": "clear sky"}]}
    analyzer = WeatherAnalyzer(weather_data)
    assert analyzer.get_weather_description() == "clear sky"