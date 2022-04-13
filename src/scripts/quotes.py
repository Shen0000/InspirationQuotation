from scraper import *

def get_quotes(categories=['Age'], keywords=['Abandon']):
    ret = []

    for category in categories:
        category = category.replace(' ', '-').replace("'", '')
        url = f"http://www.brainyquote.com/quotes/topics/{category}-quotes"
        print(url)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")

        ret += [x.text.strip() for x in soup.find_all('div',{"class" : "grid-item qb clearfix bqQt"})]

    for keyword in keywords:
        keyword = keyword.replace(' ', '-').replace("'", '')
        url = f"http://www.brainyquote.com/quotes/topics/{keyword}-quotes"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")

        ret += [x.text.strip() for x in soup.find_all('div',{"class" : "grid-item qb clearfix bqQt"})]

    return ret

if __name__ == "__main__":
    quotes = []
    authors = []
    data = get_quotes(["saint patrick's day"], [])
    # print(data)
    for quote in data:
        # print(quote.split('\n'))
        split_text = quote.split('\n')
        quotes.append(split_text[0])
        authors.append(split_text[-1])
    print(quotes, authors)
    