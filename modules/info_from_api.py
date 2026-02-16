from utils.api_request import api_request_func


def info_for_card(city_name: str):
    hour_data = api_request_func(city_name)
    for info in hour_data["list"]:
        temp = int(info["main"]["temp"])
        info_weather = info["weather"][0]["description"]
        max_temp = int(info["main"]["temp_max"])
        min_temp = int(info["main"]["temp_min"])
    timezone_offset = hour_data["city"]["timezone"]
    return city_name, temp, info_weather, max_temp, min_temp, timezone_offset