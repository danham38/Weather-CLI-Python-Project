import requests

from weather_cli.errors import (
    WeatherAPIError,
    WeatherDataError,
    WeatherTimeoutrError
)

from weather_cli.providers.base import WeatherProvider

class OpenMeteoProvider(WeatherProvider):
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    def __init__(self, timeout_seconds: int = 5):
        self.timeout_seconds = timeout_seconds

    def get_current_weather(self, lat: float, lon: float):
        params = self.build_params(lat, lon)

        response = self.make_request(params)

        data = self._parse_response(data)

        return data
    
    def build_params(lat: float, lon: float) -> dict:
        pass

    def make_request(self, params: dict):
        pass

    def _parse_response(self, response):
        pass