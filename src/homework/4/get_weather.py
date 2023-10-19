"""Get weather module. This module prompts the user for a city, retrieves real data, and then
displays a weather summary.
"""
import requests
import weather_parser

url = "https://wttr.in/Boston?format=j1"
data = requests.get(url, timeout=5)
weatherParser = weather_parser.WeatherParser(data.content.decode())
print("Enter city: Boston")
print(f"Currently feels like: {weatherParser.get_feels_like_f()} degrees F")
print(f"Current weather is: {weatherParser.get_weather_description()}")
print(f"Cloud Cover: {weatherParser.get_cloud_cover()}%")
print(f"Sunrise: {weatherParser.get_sunrise()}")
print(f"Sunset: {weatherParser.get_sunset()}")
