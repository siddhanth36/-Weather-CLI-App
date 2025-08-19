# Weather CLI App 🌤️

A command-line application built in Python that fetches and displays current weather data for any city in the world.

## Features
- Get temperature, humidity, wind speed, and weather conditions.
- Support for both Metric (°C, m/s) and Imperial (°F, mph) units.
- Clean, formatted output with emojis.
- Robust error handling for invalid cities or network issues.

## Installation & Usage

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/siddhanth36/-Weather-CLI-App.git
    cd weather-cli
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

3.  **Get a free API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).**

4.  **Run the tool:**
    *   **Method A (Recommended):** Create a file `api_key.txt` in the project directory and paste your API key into it. The script will read it automatically.
    *   **Method B:** Use the `--apikey` argument each time.
    ```bash
    # Method A (after creating api_key.txt)
    python3 weather_cli.py London

    # Method B
    python3 weather_cli.py Tokyo --units imperial --apikey YOUR_REAL_API_KEY
    ```

## How It Works
1.  The tool takes a city name and unit preference as input.
2.  It makes an HTTP GET request to the OpenWeatherMap API.
3.  It parses the returned JSON data to extract relevant weather details.
4.  It formats and prints the results to the terminal.

## Tech Stack
- Python 3
- Requests library
- OpenWeatherMap API
