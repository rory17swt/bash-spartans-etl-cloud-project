import requests 
from pymongo import MongoClient
import pprint as pp 


# Connect to local MongoDB and target the weather database and collecton
client = MongoClient()
db = client ["weather_db"]
collection = db["London_Forecast"]

# List of cities with their coordinates
cities = [
    {"name": "London", "lat": 51.5, "lon": -0.12},
    {"name": "Paris", "lat": 48.85, "lon": 2.35},
    {"name": "Berlin", "lat": 52.52, "lon": 13.41},
    {"name": "Madrid", "lat": 40.42, "lon": -3.70}
]

# List to hold all city weather documents before inserting
records = []

for city in cities:

    # Build the API URL iterating thorugh each city and coordinates
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current=temperature_2m,wind_speed_10m&timezone=Europe%2FLondon"
    
    # Fetched weather data from API
    response = requests.get(url)
    data = response.json()

    # Add the city name to the data (the API doesn't include it)
    data['city'] = city['name']

    # Append the document to the records list (builds up all city data before bulk insert)
    records.append(data)
    print(f"Fetched {city['name']}")

# Insert all the city documents into MongoDB 
collection.insert_many(records)
