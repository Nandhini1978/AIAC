import sys
import requests
import json

def display_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(url, params=params)
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    # Usage: python task1.py CITY_NAME API_KEY
    city = sys.argv[1] if len(sys.argv) > 1 else "London"
    api_key = sys.argv[2] if len(sys.argv) > 2 else "3bb70406cb4bd812163800c10bdbdfa9"
    display_weather(city, api_key)