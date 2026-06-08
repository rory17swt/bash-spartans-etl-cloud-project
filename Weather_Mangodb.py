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
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current=temperature_2m,wind_speed_10m&timezone=Europe%2FLondon"
        
        response = requests.get(url)

        # Raises an exeption if the request failed
        response.raise_for_status()

        data = response.json()
        data['city'] = city['name']
        records.append(data)

        print(f"Fetched {city['name']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {city['name']}: {e}")

    except Exception as e:
        print(f"Unexpected error for {city['name']}: {e}")

try:
    if records:
        collection.insert_many(records)
        print("Data inserted into MongoDB")

except Exception as e:
    print(f"MongoDB insert error: {e}")