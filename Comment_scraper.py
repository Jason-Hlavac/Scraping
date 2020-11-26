import requests
from bs4 import BeautifulSoup
from bs4 import Comment
scrape_comments()
def scrape_comments():
    url = input("Enter a url to scrape comments from: ")
    try:
        page = requests.get(url)
        page
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.findall
        comments = soup.find_all(string=lambda text:isinstance(text, Comment))
        print("Pretiffied Results: ")
        print("="*50)
        for c in comments:
            print(c)
            print("="*50)
            c.extract()

        print("Raw Results: ")
        print("="*50)
        print(comments)
    except: 
        print("Unable to establish a connection with the provided host.")
        print("Restarting function")
        scrape_comments()
