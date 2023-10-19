"""Test module."""
import weather_parser
import unittest


class TestWeatherParser(unittest.TestCase):
    def setUp(self):
        with open("test.json") as json_file:
            self.weather_parser = weather_parser.WeatherParser(json_file.read())

    def test_get_feels_like_f(self):
        self.assertEqual(self.weather_parser.get_feels_like_f(), "18")

    def test_get_cloud_cover(self):
        self.assertEqual(self.weather_parser.get_cloud_cover(), "50")

    def test_get_weather_description(self):
        self.assertEqual(self.weather_parser.get_weather_description(), "Partly cloudy")

    def test_get_sunrise(self):
        self.assertEqual(self.weather_parser.get_sunrise(), "07:02 AM")

    def test_get_sunset(self):
        self.assertEqual(self.weather_parser.get_sunset(), "05:56 PM")
