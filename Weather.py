import requests
import pprint as pp

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current=temperature_2m,wind_speed_10m&timezone=Europe%2FLondon"

params = {
    "latitude": 51.5,
    "longitude": -0.12,
    "current": "temperature_2m,wind_speed_10m",
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "timezone": "Europe/London"
}

response = requests.get(url, params=params)
data = response.json()

pp.pprint(data)