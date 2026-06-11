import requests
import time
from pymongo import MongoClient
import pprint as pp


client = MongoClient()
db = client["weather_db"]
collection = db["Cities_Forecast"]

cities = [
    {"name": "London", "lat": 51.5, "lon": -0.12},
    {"name": "Paris", "lat": 48.85, "lon": 2.35},
    {"name": "Berlin", "lat": 52.52, "lon": 13.41},
    {"name": "Madrid", "lat": 40.42, "lon": -3.70}
]

records = []

for city in cities:
    for attempt in range(3):  # try up to 3 times
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current=temperature_2m,wind_speed_10m&timezone=Europe%2FLondon"

            response = requests.get(url, timeout=10)  # don't hang forever
            response.raise_for_status()

            data = response.json()
            data['city'] = city['name']
            records.append(data)

            print(f"Fetched {city['name']}")
            break  # success - stop retrying

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed for {city['name']}: {e}")
            if attempt < 2:
                time.sleep(2)  # wait 2 seconds before next attempt
            else:
                print(f"Skipping {city['name']} after 3 failed attempts")

        except Exception as e:
            print(f"Unexpected error for {city['name']}: {e}")
            break  # unexpected errors aren't worth retrying

try:
    if records:
        collection.insert_many(records)
        print("Data inserted into MongoDB")

except Exception as e:
    print(f"MongoDB insert error: {e}")