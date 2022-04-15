from flask import Flask, request
import json
from quotes import *

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/get-quotes', methods=['GET'])
def getQuotes():
    search = request.args.getlist('query')
    # print(type(search))
    # print(search)
    data = get_quotes(search)
    quotes = []
    authors = []
    for quote in data:
        # print(quote.split('\n'))
        split_text = quote.split('\n')
        quotes.append(split_text[0])
        authors.append(split_text[-1])
    return json.dumps([quotes, authors])

if __name__ == "__main__":
  app.run()