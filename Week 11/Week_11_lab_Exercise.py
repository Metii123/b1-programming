import requests
import json
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #---> to make it save the json in the same folder

eu_capitals = [
    {"city": "Vienna",     "country": "Austria",     "lat": 48.2082, "lon": 16.3738},
    {"city": "Brussels",   "country": "Belgium",     "lat": 50.8503, "lon":  4.3517},
    {"city": "Sofia",      "country": "Bulgaria",    "lat": 42.6977, "lon": 23.3219},
    {"city": "Zagreb",     "country": "Croatia",     "lat": 45.8150, "lon": 15.9819},
    {"city": "Nicosia",    "country": "Cyprus",      "lat": 35.1856, "lon": 33.3823},
    {"city": "Prague",     "country": "Czechia",     "lat": 50.0755, "lon": 14.4378},
    {"city": "Copenhagen", "country": "Denmark",     "lat": 55.6761, "lon": 12.5683},
    {"city": "Tallinn",    "country": "Estonia",     "lat": 59.4370, "lon": 24.7536},
    {"city": "Helsinki",   "country": "Finland",     "lat": 60.1695, "lon": 24.9354},
    {"city": "Paris",      "country": "France",      "lat": 48.8566, "lon":  2.3522},
    {"city": "Berlin",     "country": "Germany",     "lat": 52.5200, "lon": 13.4050},
    {"city": "Athens",     "country": "Greece",      "lat": 37.9838, "lon": 23.7275},
    {"city": "Budapest",   "country": "Hungary",     "lat": 47.4979, "lon": 19.0402},
    {"city": "Dublin",     "country": "Ireland",     "lat": 53.3498, "lon": -6.2603},
    {"city": "Rome",       "country": "Italy",       "lat": 41.9028, "lon": 12.4964},
    {"city": "Riga",       "country": "Latvia",      "lat": 56.9496, "lon": 24.1052},
    {"city": "Vilnius",    "country": "Lithuania",   "lat": 54.6872, "lon": 25.2797},
    {"city": "Luxembourg", "country": "Luxembourg",  "lat": 49.6116, "lon":  6.1319},
    {"city": "Valletta",   "country": "Malta",       "lat": 35.8989, "lon": 14.5146},
    {"city": "Amsterdam",  "country": "Netherlands", "lat": 52.3676, "lon":  4.9041},
    {"city": "Warsaw",     "country": "Poland",      "lat": 52.2297, "lon": 21.0122},
    {"city": "Lisbon",     "country": "Portugal",    "lat": 38.7223, "lon": -9.1393},
    {"city": "Bucharest",  "country": "Romania",     "lat": 44.4268, "lon": 26.1025},
    {"city": "Bratislava", "country": "Slovakia",    "lat": 48.1486, "lon": 17.1077},
    {"city": "Ljubljana",  "country": "Slovenia",    "lat": 46.0569, "lon": 14.5058},
    {"city": "Madrid",     "country": "Spain",       "lat": 40.4168, "lon": -3.7038},
    {"city": "Stockholm",  "country": "Sweden",      "lat": 59.3293, "lon": 18.0686},
]

WEATHER_CODES = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Icy fog", 51: "Light drizzle", 53: "Drizzle",
    55: "Heavy drizzle", 61: "Slight rain", 63: "Rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Snow", 75: "Heavy snow", 80: "Slight showers",
    81: "Showers", 82: "Heavy showers", 95: "Thunderstorm",
}

def fetch_weather(city):
    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude":        city["lat"],
                "longitude":       city["lon"],
                "current_weather": True,
                "hourly":          "temperature_2m,precipitation_probability,weathercode",
                "forecast_days":   1,
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        cw = data["current_weather"]
        hourly = data["hourly"]

        return {
            "country":     city["country"],
            "coordinates": {"latitude": city["lat"], "longitude": city["lon"]},
            "current_weather": {
                "temperature": cw["temperature"],
                "windspeed":   cw["windspeed"],
                "weathercode": cw["weathercode"],
                "condition":   WEATHER_CODES.get(cw["weathercode"], "Unknown"),
                "time":        cw["time"],
            },
            "hourly_forecast": [
                {
                    "time":                      hourly["time"][i],
                    "temperature":               hourly["temperature_2m"][i],
                    "precipitation_probability": hourly["precipitation_probability"][i],
                    "weathercode":               hourly["weathercode"][i],
                }
                for i in range(len(hourly["time"]))
            ],
        }

    except Exception as e:
        print(f"[ERROR]: {city['city']} - {e}")
        return None

results = {}

for capital in eu_capitals:
    print(f"[LOG]: Fetching - {capital['city']}, {capital['country']}...")
    data = fetch_weather(capital)
    if data:
        results[capital["city"]] = data
    time.sleep(0.5)

with open("eu_weather_data.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\n[LOG]: Done - {len(results)}/{len(eu_capitals)} cities saved to eu_weather_data.json.")
