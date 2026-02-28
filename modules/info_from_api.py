from utils.api_request import api_request_func


def info_for_card(city_name: str):
    data = api_request_func(city_name)  # почасовой прогноз
    first = data["list"][0]  # берем первый час

    temp = int(first["main"]["temp"])
    max_temp = int(first["main"]["temp_max"])
    min_temp = int(first["main"]["temp_min"])
    info_weather = first["weather"][0]["description"]
    timezone_offset = data["city"]["timezone"]
    icon = first["weather"][0]["description"]
    icon_dict ={
        "чисте небо": "sun.png",
        "легкий дощ": "light_rain.png",
        "уривчасті хмари": "07Cloudy.png",
        "рвані хмари": "more_cloud.png",
        "хмарно": "cloud.png",
        "дощ": "rain.png",
        "гроза": "thenderstorm.png",
        "сніг": "snow.png",
        "туман": "fog.png"
    }
    icon_get = icon_dict[icon]
    # print(icon_get)
    return city_name, temp, info_weather, max_temp, min_temp, timezone_offset, icon_get