import requests, json

from config import API_KEY


def api_request_func(city_name: str):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&units=metric&appid={API_KEY}&lang=UA&units=metric")
    data_dict = response.json()
    return data_dict


def api_request_city():
    response = requests.get(f"https://countriesnow.space/api/v0.1/countries/population/cities")
    data_dict = response.json()
    # premennea = json.dump(data_dict, indent=4, ensure_ascii=False)
    # print(data_dict)
    return data_dict