# WeatherPY

WeatherPY is a simple command-line weather application built with Python. It lets you enter a city name and displays the current weather conditions, temperature, humidity, and location details in a friendly terminal output.

## Features

- Fetch live weather information from OpenWeatherMap
- Cache recent weather lookups in a SQLite database to reduce API requests and save your requests
- Display temperature, humidity, and weather conditions
- Friendly CLI experience with colorful output
- Simple setup and quick usage

## Requirements

Make sure you have Python 3 installed. It is recommended to create a venv to make sure that global packages stays unedited.

Creating a venv:
```bash
python -m venv .venv
```

Activate the venv:
1) Windows: ```.venv\Scripts\activate```
2) Mac/Linux: ```source .venv/bin/activate```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Rename or copy `config.example.py` to `config.py`
2. Replace `YOUR_API_KEY_HERE` with your OpenWeatherMap API key
3. Optionally adjust the app name, version, or debug settings

Example:

```python
APP_NAME = "WeatherPY"
APP_VERSION = "1.0.0"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "your_real_api_key"
DB_PATH = "database/weather.db"
DEBUG = False
```

The app now uses the SQLite cache file defined by `DB_PATH` to store recent weather responses for faster repeated lookups.

Quick Tip: You can enable the DEBUG in config. When the app runs, you will automatically get the time taken for the request to complete.

## Usage

Run the application with:

```bash
python -m main
```

When prompted, enter the name of a city. You can type `quit`, `exit`, or `stop` to leave the program.

## Project Structure

- `main.py` - Entry point for the CLI application
- `config.py` - Application configuration
- `utils/api_client.py` - Handles requests to the weather API
- `utils/formatter.py` - Formats and displays weather data
- `utils/db_manager.py` - Implements the SQLite-based caching layer

## Future Updates

The caching system is now implemented. Upcoming enhancements include:

- A more polished and interactive user interface built with Python's Textual library
- Better search history and saved preferences
- Improved error handling and more detailed weather summaries

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it in accordance with the terms of the license.