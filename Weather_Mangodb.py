import requests 
from pymongo import MongoClient
import pprint as pp 


client = MongoClient()
db = client ["weather_db"]
collection = db["London_Forecast"]

cities = [
    {"name": "London", "lat": 51.5, "lon": -0.12},
    {"name": "Paris", "lat": 48.85, "lon": 2.35},
    {"name": "Berlin", "lat": 52.52, "lon": 13.41},
    {"name": "Madrid", "lat": 40.42, "lon": -3.70}
]

records = []

for city in cities:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current=temperature_2m,wind_speed_10m&timezone=Europe%2FLondon"
    
    response = requests.get(url)
    data = response.json()
    data['city'] = city['name']
    records.append(data)
    print(f"Fetched {city['name']}")

collection.insert_many(records)
