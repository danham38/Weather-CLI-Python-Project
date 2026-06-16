from  abc import ABC, abstractmethod

class WeatherProvider(ABC):

    @abstractmethod
    def get_current_weather(self, lat: float, lon: float):
        return