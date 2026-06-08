import os
import json

with open("weather_data.json", "r") as file:
    data = json.load(file)

if len(data) == 4:
    print("Success: The file has data for all 4 cities!")
else:
    print("Error: The number of cities is wrong.")

expected_cities = ["London", "Paris", "Berlin", "Madrid"]

found_cities = [data[0]["city"], data[1]["city"], data[2]["city"], data[3]["city"]]

if found_cities == expected_cities:
    print("Success: All 4 cities (London, Paris, Berlin, Madrid) are correct and in order!")
else:
    print("Error: The city names are incorrect or out of order.")