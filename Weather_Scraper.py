from bs4 import BeautifulSoup
import requests

page = requests.get("https://weather.com/weather/today/l/USCA1209:1:US")
soup = BeautifulSoup(page.content, "html.parser")
temperature= soup.find("div", class_="today_nowcard-temp").get_text()

page = requests.get("https://weather.com/weather/tenday/l/USCA1209:1:US")
soup = BeautifulSoup(page.content, "html.parser")
city = soup.find("div", class_="locations-title ten-day-page-title").get_text()
days = soup.find("span", class_="date-time").get_text()
city = city.replace("10 Day Weather5:32 pm PDTPrint", " ", 1)
print("Weather forecast for {} \nCurrent Temperature: {}\n{}".format(city, temperature, days))
