import requests
import json


def give_info():
    wy_weather = requests.get("https://api.weather.gov/gridpoints/RIW/105,86/forecast")
    information = wy_weather.json()

    day_1 = information["properties"]["periods"][0]["name"]
    day_1_temp = information["properties"]["periods"][0]["temperature"]
    day_1_wind_speed = information["properties"]["periods"][0]["windSpeed"]
    day_1_wind_direction = information["properties"]["periods"][0]["windDirection"]
    day_1_forecast = information["properties"]["periods"][0]["detailedForecast"]

    day_2 = information["properties"]["periods"][1]["name"]
    day_2_temp = information["properties"]["periods"][1]["temperature"]
    day_2_wind_speed = information["properties"]["periods"][1]["windSpeed"]
    day_2_wind_direction = information["properties"]["periods"][1]["windDirection"]
    day_2_forecast = information["properties"]["periods"][1]["detailedForecast"]

    day_3 = information["properties"]["periods"][2]["name"]
    day_3_temp = information["properties"]["periods"][2]["temperature"]
    day_3_wind_speed = information["properties"]["periods"][2]["windSpeed"]
    day_3_wind_direction = information["properties"]["periods"][2]["windDirection"]
    day_3_forecast = information["properties"]["periods"][2]["detailedForecast"]

    text=f"""{day_1}: {day_1_temp} F
{day_1_wind_speed} {day_1_wind_direction}
{day_1_forecast}

{day_2}: {day_2_temp} F
{day_2_wind_speed} {day_2_wind_direction}
{day_2_forecast}

{day_3}: {day_3_temp} F
{day_3_wind_speed} {day_3_wind_direction}
{day_3_forecast}
    """
    return text