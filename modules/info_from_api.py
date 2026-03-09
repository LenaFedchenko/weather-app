from utils.api_request import api_request_func


def info_for_card(city_name: str):
    data = api_request_func(city_name)  # почасовой прогноз
    first = data["list"][0]  # берем первый час

    temp = int(first["main"]["temp"])
    # print(temp)
    max_temp = int(first["main"]["temp_max"])
    min_temp = int(first["main"]["temp_min"])
    info_weather = first["weather"][0]["description"]
    timezone_offset = data["city"]["timezone"]
    icon = first["weather"][0]["icon"]
    # print(icon)
    icon_dict ={
        "01d": "01d.png",
        "02d": "02d.png",
        "03d": "03d.png",
        "04d": "04d.png",
        "09d": "09d.png",
        "10d": "10d.png",
        "11d": "11d.png",
        "13d": "13d.png",
        "50d": "50d.png",
        "01n": "01n.png",
        "02n": "02n.png",
        "03n": "03n.png",
        "04n": "04n.png",
        "09n": "09n.png",
        "10n": "10n.png",
        "11n": "11n.png",
        "13n": "13n.png",
        "50n": "50n.png"
    }
    icon_get = icon_dict[icon]
    return city_name, temp, info_weather, max_temp, min_temp, timezone_offset, icon_get