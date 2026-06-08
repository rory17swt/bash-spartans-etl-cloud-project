# Bash Spartans ETL Cloud Project

## Overview
A Python-based ETL pipeline that extracts live weather data from the Open Meteo API, 
stores it in MongoDB, serializes it to JSON, and uploads it to AWS S3.

## Pipeline
```
API -> Python -> MongoDB -> JSON -> S3
```

## Process

### 1. Finding the API
We used the [Open Meteo API](https://open-meteo.com), this API returns live weather data in JSON format.

### 2. Fetching the Data
We started by fetching weather data for London and printing it in Python to verify the API was working.

```python
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current=temperature_2m,wind_speed_10m&timezone=Europe%2FLondon"

response = requests.get(url)
data = response.json()

print(data)
```

### 3. Fetching Multiple Cities

![Open Meteo API](images/api-coordinates.png)

Using the base URL we couldn't fetch data for multiple cities...

Using the base URL we couldn't fetch data for multiple cities. Instead, we created a `for` loop that iterates through a `cities` list, building a dynamic URL for each city using an f-string.

```python
import requests

cities = [
    {"name": "London", "lat": 51.5, "lon": -0.12},
    {"name": "Paris", "lat": 48.85, "lon": 2.35},
    {"name": "Berlin", "lat": 52.52, "lon": 13.41},
    {"name": "Madrid", "lat": 40.42, "lon": -3.70}
]

for city in cities:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={city['lat']}&longitude={city['lon']}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&current=temperature_2m,wind_speed_10m&timezone=Europe%2FLondon"
    
    response = requests.get(url)
    data = response.json()
    data['city'] = city['name']
    
    print(city['name'], data['current'])
```

Each iteration fetches one city, adds the city name to the response, and prints the current weather. This gave us clean data for all four cities.