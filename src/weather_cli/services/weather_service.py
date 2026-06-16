from weather_cli.providers.base import WeatherProvider

class WeatherService:
    def __init__(self, provider: WeatherProvider):
        self.provider = provider

    def get_weather(self, lat: float, lon: float):
        pass