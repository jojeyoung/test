from weather_model import WeatherModel
from bs4 import BeautifulSoup
import requests


def weather_title(today="날씨"):
    url = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query={today}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    target = soup.select_one('.todaytemp')
    print(target.text)
    return target.text
