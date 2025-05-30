import os
import requests
from dotenv import load_dotenv
from langchain.tools import Tool

load_dotenv()

def get_weather(city):
    # Get latitude and longitude
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_res = requests.get(geo_url).json()
    if not geo_res.get("results"):
        return f"Sorry, I couldn't find the location {city}."

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Get current weather in Fahrenheit
    weather_url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "temperature_unit": "fahrenheit"
    }
    weather_res = requests.get(weather_url, params=params).json()
    temp = weather_res.get("current_weather", {}).get("temperature")

    if temp is None:
        return f"Sorry, no weather data available for {city}."
    return f"The current temperature in {city} is {temp}°F."

weather_tool = Tool.from_function(
    func=get_weather,
    name="WeatherInfo",
    description="Get current weather details for a specific city."
)
