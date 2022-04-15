from scraper import *

def get_quotes(searches=[]):
    ret = []

    for search in searches:
        search = search.replace(' ', '-').replace("'", '')
        url = f"http://www.brainyquote.com/quotes/topics/{search}-quotes"
        # print(url)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")

        ret += [x.text.strip() for x in soup.find_all('div',{"class" : "grid-item qb clearfix bqQt"})]

    return ret

def get_quotes_by_author(authors=[]):
    ret = []

    for search in authors:
        search = search.replace(' ', '-').replace("'", '')
        url = f"http://www.brainyquote.com/quotes/{search}"
        # print(url)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")

        ret += [x.text.strip() for x in soup.find_all('div',{"class" : "grid-item qb clearfix bqQt"})]

    return ret

if __name__ == "__main__":
    quotes = []
    authors = []
    data = get_quotes(["memory"])
    # print(data)
    for quote in data:
        # print(quote.split('\n'))
        split_text = quote.split('\n')
        quotes.append(split_text[0])
        authors.append(split_text[-1])
    print(quotes, authors)
    