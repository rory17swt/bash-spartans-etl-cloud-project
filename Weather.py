import requests
import pprint as pp


# List of cities with coordinates
cities = [
    {"name": "London", "lat": 51.5, "lon": -0.12},
    {"name": "Paris", "lat": 48.85, "lon": 2.35},
    {"name": "Berlin", "lat": 52.52, "lon": 13.41},
    {"name": "Madrid", "lat": 40.42, "lon": -3.70}
]

for city in cities:
    # Build the API URL iterating thorugh each city and coordinates
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current=temperature_2m,wind_speed_10m&timezone=Europe%2FLondon"
    
    # Fetch the weather data from the API
    response = requests.get(url)

    # Parse the JSON response into a Python dictionary
    data = response.json()

    # Add the city name to the data (The API response doesn't include it)
    data['city'] = city['name']
    
    print("successful")