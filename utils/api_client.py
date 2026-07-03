import requests
import json
from colorama import Back, Fore, Style, init
from config import BASE_URL, API_KEY

#intialize colorama
init(autoreset=True)

def get_weather_info(city: str):
    """
    Provides the weather update by passing the city name as arguments.
    """
    try:
        data = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
        data.raise_for_status()
        output_json = data.json()
        return output_json
    except requests.exceptions.ConnectionError:
        print(Back.YELLOW + Fore.RED + " ERROR: INTERNET NOT CONNECTED! " + Style.RESET_ALL)
        return None
    except requests.exceptions.HTTPError:
        print(Back.YELLOW + Fore.RED + " ERROR: CITY CANNOT BE FOUND! " + Style.RESET_ALL)
        return None
    except Exception as e:
        print(Back.YELLOW + Fore.RED + f" ERROR: {e}" + Style.RESET_ALL)
        return None
    
data = get_weather_info("patna, india")
with open("test.json", "w") as f:
    json.dump(data,f, indent=4)