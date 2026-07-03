import time
import sys
import random
from colorama import Fore, Back, Style, init
from config import DEBUG, APP_VERSION, APP_NAME
from utils.api_client import get_weather_info
from utils.formatter import display_weather

# initialize colorama
init(autoreset=True)

def typing_speed(text: str, speed:float =0.04, end: bool = False):
    """
    creates a typing effect on the string passed to it, takes three arguments: text, speed and end. Default speed is 0.04 and default end is false.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    if end == True:
        print(end="")
    else:
        print()

def loading_dots(text: str, remove_text:bool =False):
    """Creates a loading dots effect on the string passed to it.

    If remove_text is True, it completely wipes the line after finishing.
    """
    duration = random.randint(2,5)
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(4):
            dots = "."*i
            sys.stdout.write(f"\r\033[K{text}{dots}")
            sys.stdout.flush()
            time.sleep(0.4)

    if remove_text:
        sys.stdout.write("\r\033[K")
    else:
        sys.stdout.write("\n")
    sys.stdout.flush()

# ----- main code ----- #
def main():
    print("-"*50)
    typing_speed(f"Welcome to {APP_NAME}! Get the latest weather updates instantly.")
    typing_speed("Tip: You can type 'help' to know more.")
    if DEBUG:
        typing_speed(f"APP VERSION: {APP_VERSION}")
    while True:
        typing_speed("Enter the name of the city: ", end=True)
        user_input = input(">> ").lower()
        exit_list = ["quit", "exit", "stop"]
        if user_input in exit_list:
            typing_speed(f"Thanks for visiting {APP_NAME}!")
            break
        typing_speed("fetching the weather update, please wait.")
        loading_dots("Extracting",remove_text=True)
        data = get_weather_info(user_input)
        if isinstance(data, dict):
            display_weather(data)
        else:
            continue

if __name__ == "__main__":
    main()