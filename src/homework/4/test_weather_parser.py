"""Test module."""
import weather_parser
import unittest


class TestWeatherParser(unittest.TestCase):
    def setUp(self):
        with open("test_data.json") as json_file:
            self.weather_parser = weather_parser.WeatherParser(json_file.read())

    def test_get_feels_like_f(self):
        self.assertEqual(self.weather_parser.get_feels_like_f(), "56")

    def test_get_cloud_cover(self):
        self.assertEqual(self.weather_parser.get_cloud_cover(), "100")

    def test_get_weather_description(self):
        self.assertEqual(self.weather_parser.get_weather_description(), "Light rain, mist")

    def test_get_sunrise(self):
        self.assertEqual(self.weather_parser.get_sunrise(), "07:04 AM")

    def test_get_sunset(self):
        self.assertEqual(self.weather_parser.get_sunset(), "05:53 PM")
