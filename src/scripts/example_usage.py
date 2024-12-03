from weather_insights import fetch_weather_data, WeatherAnalyzer, WeatherVisualizer

def main():
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    city = "New York"

    try:
        weather_data = fetch_weather_data(city, API_KEY)
        analyzer = WeatherAnalyzer(weather_data)
        visualizer = WeatherVisualizer(analyzer)
        visualizer.display_weather()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
