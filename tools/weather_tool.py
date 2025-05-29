from langchain.tools import Tool
import requests

def get_weather(city):
    geocode = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}").json()
    if not geocode.get("results"):
        return f"No coordinates found for {city}."
    lat = geocode["results"][0]["latitude"]
    lon = geocode["results"][0]["longitude"]
    weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true").json()
    current = weather.get("current_weather", {})
    return f"{city}: {current.get('temperature', 'N/A')}°C, Wind {current.get('windspeed', 'N/A')} km/h."

weather_tool = Tool.from_function(
    func=get_weather,
    name="Weather",
    description="Get current weather details for a specific city."
)