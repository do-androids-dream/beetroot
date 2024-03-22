"""Write a console application which takes as an input a city name and returns current weather in the format of your choice.
For the current task, you can choose any weather API or website or use openweathermap.org """

import requests

URL = "https://weatherapi-com.p.rapidapi.com/current.json"


def welcome():
    print("===========WELCOME=============")
    city = input("enter the city name: ")
    return city


def print_response(response):
    print(response["location"]["name"], ", ", response["location"]["country"])
    print(f"current temp: {response["current"]["temp_c"]} C")
    print(f"condition: {response["current"]["condition"]["text"]}")
    print(f"humidity: {response["current"]["humidity"]}")
    print(f"wind: {response["current"]["wind_kph"]} km/h")


def run_app():
    while True:
        city = welcome()
        querystring = {"q": city}

        headers = {
            "X-RapidAPI-Key": "ad9a355609msh08b1aaec50db857p15e314jsn53d9bbe1dab3",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }
        try:
            response = requests.get(URL, headers=headers, params=querystring).json()
            print_response(response)
        except KeyError:
            print("can't find such city")



if __name__ == '__main__':
    run_app()

