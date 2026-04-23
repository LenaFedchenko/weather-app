from utils.api_request import api_request_func, api_request_city, api_request_geo

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
    try:
        icon_get = icon_dict[icon]
    except:
        icon_get = icon_dict["01d"]
    return city_name, temp, info_weather, max_temp, min_temp, timezone_offset, icon_get


def info_cityes():
    list_city = []
    api_request = api_request_city()
    for i in api_request["data"]:
        list_city.append(i["city"])
    return list_city
def info_country():
    list_country = []
    api_request = api_request_city()
    for country in api_request["data"]:
        if country["country"] not in list_country:
            list_country.append(country["country"])
    list_country = list_country[1:]
    # print(list_country)
    return list_country

def info_city_from_coutry(coutry):
    list_city = []
    api_request = api_request_city()
    for country_gotten in api_request["data"]:
        if country_gotten["country"] == coutry:
            list_city.append(country_gotten["city"])
    return list_city
def info_geo(city_name):
    try:
        api_request = api_request_geo(city_name)
        # print(api_request)
        length_coordiantes = api_request[0]['lat']
        width_coordinates = api_request[0]['lon']
    except Exception as error:
        print(error)
    return length_coordiantes, width_coordinates
