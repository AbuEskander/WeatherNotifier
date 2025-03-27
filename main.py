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



def main():
        load_dotenv()
        
        lat, long = get_current_location()
        API_KEY = os.getenv("API_KEY")  # Replace with your valid API key from OpenWeatherMap
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_KEY}&units=metric")
        print(res.json())
        with open("Weather.json","w") as file: # These 2 lines are just for debuging and visualizing the Json file, I don't know a better way yet :P
                json.dump(res.json(),file,indent=4)
        temp = res.json()["main"]["temp"]
        print(temp)





if __name__ == "__main__":
        main()