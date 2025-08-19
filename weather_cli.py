import requests
import argparse
import json
from datetime import datetime

# Your OpenWeatherMap API Key (CRITICAL: Replace this with your own key!)
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city_name, units='metric'):
    """
    Fetches weather data from the OpenWeatherMap API.
    Returns a JSON response or None if the request fails.
    """
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': units  # 'metric' for Celsius, 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raises an exception for HTTP errors (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(data, units='metric'):
    """
    Parses the JSON data and displays it in a user-friendly format.
    """
    if data is None:
        print("No data to display.")
        return

    # Check if the API returned an error code (e.g., city not found)
    if data.get('cod') != 200:
        print(f"Error: {data.get('message', 'Unknown error')}")
        return

    # Extract relevant information
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    weather_desc = data['weather'][0]['description'].title()
    wind_speed = data['wind']['speed']

    # Determine the unit symbols
    temp_unit = '°C' if units == 'metric' else '°F'
    speed_unit = 'm/s' if units == 'metric' else 'mph'

    # Get the current time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the weather information
    print("\n" + "="*40)
    print(f"Weather in {city}, {country}")
    print(f"As of: {now}")
    print("="*40)
    print(f"🌡️  Temperature: {temp}{temp_unit} (Feels like {feels_like}{temp_unit})")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️  Wind: {wind_speed} {speed_unit}")
    print(f"☁️  Conditions: {weather_desc}")
    print("="*40)

def main():
    """
    Main function to handle command-line arguments and execute the program.
    """
    parser = argparse.ArgumentParser(description="Get the current weather for any city.")
    parser.add_argument('city', type=str, help="Name of the city to get weather for")
    parser.add_argument('--units', '-u', type=str, choices=['metric', 'imperial'], default='metric',
                        help="Unit system: 'metric' (Celsius) or 'imperial' (Fahrenheit). Default is metric.")
    parser.add_argument('--apikey', '-a', type=str, help="Optionally specify your API key here instead of in the script.")

    args = parser.parse_args()

    # Use the API key from command line if provided, else use the one in the script
    global API_KEY
    if args.apikey:
        API_KEY = args.apikey

    if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
        print("Error: API key is not set.")
        print("Please get a free API key from https://openweathermap.org/api and:")
        print("  1. Replace 'YOUR_API_KEY_HERE' in the script, OR")
        print("  2. Use the --apikey argument when running the script.")
        print("\nExample: python3 weather_cli.py London --apikey YOUR_REAL_API_KEY")
        return

    # Get the weather data
    weather_data = get_weather_data(args.city, args.units)

    # Display the results
    if weather_data:
        display_weather(weather_data, args.units)
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
