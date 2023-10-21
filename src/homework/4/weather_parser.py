"""Weather parser module."""
import json
from typing import Dict, Any


class WeatherParser:
    """Weather parser."""

    def __init__(self, json_str: str):
        # Original data in a form of Python object
        original: Dict[str, Any] = json.loads(json_str)

        # extract key data
        current_condition: Dict[str, Any] = original["current_condition"][0]
        astronomy = original["weather"][0]["astronomy"][0]
        self.data = {
            "feelsLikeF": current_condition["FeelsLikeF"],
            "cloudCover": current_condition["cloudcover"],
            "weatherDescription": current_condition["weatherDesc"][0]["value"],
            "sunset": astronomy["sunset"],
            "sunrise": astronomy["sunrise"],
        }

    def get_feels_like_f(self) -> str:
        """Returns the FeelsLikeC indicator."""
        return self.data["feelsLikeF"]

    def get_cloud_cover(self) -> str:
        """Returns the cloud cover indicator."""
        return self.data["cloudCover"]

    def get_weather_description(self) -> str:
        """Returns the weather description."""
        return self.data["weatherDescription"]

    def get_sunset(self) -> str:
        """Returns the sunset time."""
        return self.data["sunset"]

    def get_sunrise(self) -> str:
        """Returns the sunrise time."""
        return self.data["sunrise"]
