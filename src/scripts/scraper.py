from bs4 import BeautifulSoup
import json
import requests
import re

def get_categories():

    url = "http://www.brainyquote.com/quotes/topics.html"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")

    ret = [x.text.strip() for x in soup.find_all('a',{"href" : re.compile("/topics/")})]
    return ret


if __name__ == "__main__":
    categories = get_categories() # gets all categories on brainyquote.com/topics
    print(categories)