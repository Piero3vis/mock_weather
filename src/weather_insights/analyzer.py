class WeatherAnalyzer:
    def __init__(self, weather_data: dict):
        self.weather_data = weather_data

    def get_temperature_celsius(self) -> float:
        """Get the temperature in Celsius."""
        kelvin = self.weather_data["main"]["temp"]
        return kelvin - 273.15

    def get_weather_description(self) -> str:
        """Get the weather description."""
        return self.weather_data["weather"][0]["description"]