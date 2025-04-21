import requests

#url = "http://127.0.0.1:8000/predict"      # Local
url = "http://34.201.50.77:8000/predict"    # Deploy Nube

data = {
    "YEAR": 2024,
    "MONTH": 4,
    "DAY": 20,
    "DAY_OF_WEEK": 6,
    "AIRLINE": 3,
    "ORIGIN_AIRPORT": 10,
    "DESTINATION_AIRPORT": 45,
    "SCHEDULED_DEPARTURE": 830,
    "DEPARTURE_TIME": 845,
    "DEPARTURE_DELAY": 15.0,
    "TAXI_OUT": 10.0,
    "WHEELS_OFF": 855,
    "SCHEDULED_TIME": 120.0,
    "ELAPSED_TIME": 115.0,
    "AIR_TIME": 100.0,
    "DISTANCE": 1500.0,
    "WHEELS_ON": 955,
    "TAXI_IN": 5.0,
    "SCHEDULED_ARRIVAL": 950,
    "ARRIVAL_TIME": 960,
    "DIVERTED": 0,
    "AIR_SYSTEM_DELAY": 5.0,
    "SECURITY_DELAY": 0.0,
    "AIRLINE_DELAY": 10.0,
    "LATE_AIRCRAFT_DELAY": 0.0,
    "WEATHER_DELAY": 0.0
}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Predicción:", response.json())