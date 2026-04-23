import requests, json
from config import API_KEY
import config


def api_request_func(city_name: str):
    if config.LANGUAGE == "uk":
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={API_KEY}&lang=UA&units=metric&lang=ua")
    else:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={API_KEY}&lang=en&units=metric&lang=en")
    data_dict = response.json()
    return data_dict


def api_request_city():
    response = requests.get(f"https://countriesnow.space/api/v0.1/countries/population/cities")
    data_dict = response.json()
    return data_dict

def api_request_geo(city_name):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}")
    data_dict = response.json()
    return data_dict
