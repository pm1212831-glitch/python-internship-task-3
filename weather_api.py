
import requests
import json
from pathlib import Path


def get_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=21.1458&longitude=79.0882"
        "&current=temperature_2m,relative_humidity_2m"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        json_path = Path(__file__).resolve().parent / "weather.json"

        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        current = data["current"]

        print("\n=== Nagpur Weather ===")
        print(f"Temperature: {current['temperature_2m']} °C")
        print(f"Humidity: {current['relative_humidity_2m']}%")
        print("Weather data saved to api/weather.json")

    except (requests.RequestException, KeyError, ValueError) as error:
        print(f"Unable to fetch weather data: {error}")


if __name__ == "__main__":
    get_weather()


