class WeatherVisualizer:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def display_weather(self):
        """Display the weather in a readable format."""
        temp = self.analyzer.get_temperature_celsius()
        description = self.analyzer.get_weather_description()
        print(f"The current temperature is {temp:.2f}°C and the weather is {description}.")