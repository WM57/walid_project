import requests


def try_me():
    return print('Décollage immédiat')


def weather(ville):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={ville}&appid=dae9a5019961ec753439f157ed0e1221'
    ).json()
    c = response['main']['temp'] - 273.15

    return c
