#Todo : Weather Notifier using Python
#Author : Basil Ismail (AbuEskander)

from dotenv import load_dotenv
import  geocoder
import requests
import json
import os


def get_current_location()-> tuple[int, int]:
        current_location = geocoder.ip("me")
        if current_location.latlng:
                lat,long = current_location.latlng
        return lat,long

def tele_message(message:str):
        TELE_KEY = os.getenv("TELE_KEY")
        url = f'https://api.telegram.org/bot{TELE_KEY}/sendMEssage?chat_id={os.getenv("CHAT_ID")}&text={message}'
        res = requests.post(url)
        print(res.json())

def main():        
        lat, long = get_current_location()
        API_KEY = os.getenv("API_KEY")  # Replace with your valid API key from OpenWeatherMap
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_KEY}&units=metric")
        with open("Weather.json","w") as file: # These 2 lines are just for debuging and visualizing the Json file, I don't know a better way yet :P
                json.dump(res.json(),file,indent=4)
        main = res.json()["main"]
        weather = res.json()["weather"]
        tele_message(f"Hey there, the temp is {main["temp"]}°C, but feels like {main["feels_like"]}°C")
        tele_message(f"The sky is {weather[0]["description"]}")



if __name__ == "__main__":
        load_dotenv()
        main()