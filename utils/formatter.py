from colorama import Fore, Style
from .api_client import get_weather_info

def display_weather(weather_data: dict):
    city_name = weather_data["name"]
    country = weather_data["sys"]["country"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    condition = weather_data["weather"][0]["description"]
    print(Fore.CYAN + "========================================" + Style.RESET_ALL)
    print(f"🌍 Location:   {city_name}, {country}")
    print(f"🌡️  Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"💧 Humidity:    {humidity}%")
    print(f"☁️  Condition:   {condition.title()}")
    print(Fore.CYAN + "========================================" + Style.RESET_ALL)