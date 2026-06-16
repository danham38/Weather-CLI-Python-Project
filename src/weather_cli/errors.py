class LatitudeValidationError(Exception):
    def __init__(self, message, lat, error_code = 400):
        self.lat = lat
        self.error_code = error_code
        self.message = f"Invalid latitude: {lat}. Latitude must be between -90 and 90 inclusive"
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error code: {self.error_code})"
    
def check_invalid_lat(lat):
    if (-90>lat or lat>90):
        raise LatitudeValidationError(lat)
    
class LongitudeValidationError(Exception):
    def __init__(self, message, long, error_code = 400):
        self.long = long
        self.message = f"Invalid Longitiude: {long}. Longitude must be between -180 and 180 inclsuive."
        self.error_code = error_code
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error code: {self.error_code})"
    
def check_invalid_long(long):
    if (-180>long or 180<long):
        raise LongitudeValidationError(long)
    
class WeatherTimeoutrError(Exception):
    def __init__(self, message, error_code = 408):
        self.message = "API Timeout"
        self.error_code = error_code
        super().__init__(message)
        
    def __str__(self):
        return f"{self.message}. (Error code: {self.error_code})"
    
class WeatherAPIError(Exception):
    def __init__(self, message, error_code = 502):
        self.message = f"API returned bad status"
        self.error_code = error_code
        super().__init__(message)

    def __str__(self):
        return f"{self.message}. Error code {self.error_code}"
    
class WeatherDataError(Exception):
    def __init__(self, message, error_code = 400):
        self.message = f"Data error"
        self.error_code = error_code
        super().__init__(message)

    def __str__(self):
        return f"{self.message} Error code {self.error_code}"