from bs4 import BeautifulSoup
import requests

page = requests.get("https://weather.com/weather/today/l/USCA1209:1:US")
soup = BeautifulSoup(page.content, "html.parser")
temperature= soup.find("div", class_="today_nowcard-temp").get_text()

page = requests.get("https://weather.com/weather/tenday/l/USCA1209:1:US")
soup = BeautifulSoup(page.content, "html.parser")
city = soup.find("div", class_="locations-title ten-day-page-title").get_text()
tenday = soup.find("section", class_="panel ls-24-hour-wrap twc-table-wrap card forecast-fiveday").get_text()
city.replace("10 Day Weather", "", 1)
print("Weather forecast for {} \nCurrent Temperature: {}\n{}".format(city, temperature, tenday))
