import requests

from config import API_KEY


def api_request_func(city_name: str):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={API_KEY}&lang=UA&units=metric")
    data_dict = response.json()
    return data_dict
