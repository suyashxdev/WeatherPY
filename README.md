# WeatherPY

WeatherPY is a simple command-line weather application built with Python. It lets you enter a city name and displays the current weather conditions, temperature, humidity, and location details in a friendly terminal output.

## Features

- Fetch live weather information from OpenWeatherMap
- Display temperature, humidity, and weather conditions
- Friendly CLI experience with colorful output
- Simple setup and quick usage

## Requirements

Make sure you have Python 3 installed, then install the required packages:

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
DEBUG = False
```

## Usage

Run the application with:

```bash
python main.py
```

When prompted, enter the name of a city. You can type `quit`, `exit`, or `stop` to leave the program.

## Project Structure

- `main.py` - Entry point for the CLI application
- `config.py` - Application configuration
- `utils/api_client.py` - Handles requests to the weather API
- `utils/formatter.py` - Formats and displays weather data

## Future Updates

Planned enhancements for upcoming releases include:

- A caching system to reduce repeated API requests and improve performance
- SQLite database integration for storing recent searches and weather history
- Improved error handling and more detailed weather summaries

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute it in accordance with the terms of the license.