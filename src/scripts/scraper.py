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

def get_keywords_paths():

    url = "http://www.brainyquote.com/quotes/topics.html"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")

    ret = [x.get('href').strip() for x in soup.find_all('a',{"href" : re.compile("/topic_index/")})]
    return ret

def get_keywords(paths):
    ret =  []

    for path in paths:
        url = f"http://www.brainyquote.com{path}"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")

        tmp = [x.text.strip() for x in soup.find_all('span',{"class": "authorContentName"})]
        for keyword in tmp:
            ret.append(keyword)
    return ret

if __name__ == "__main__": 
    
    ''' DON'T RUN CODE SEGMENT! Only run if json data needs to be updated

    categories = get_categories() # gets all categories on brainyquote.com/topics
    jsonCategories = json.dumps(categories)
    with open('src/assets/categories.json', 'w') as outfile:
        json.dump(jsonCategories, outfile)

    keyword_paths = get_keywords_paths()
    jsonPaths = json.dumps(keyword_paths)
    with open('src/assets/paths.json', 'w') as outfile:
        json.dump(jsonPaths, outfile)

    keywords = get_keywords(keyword_paths)
    jsonKeywords = json.dumps(keywords)
    with open('src/assets/keywords.json', 'w') as outfile:
        json.dump(jsonKeywords, outfile)

    '''

