from bs4 import BeautifulSoup
import requests
page = requests.get("https://weather.com/weather/today/l/USCA1209:1:US")
soup = BeautifulSoup(page.content, "html.parser")
soup.find_all("div", class_="today_nowcard-temp")
