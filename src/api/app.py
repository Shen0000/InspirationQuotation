from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from quotes import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/get-quotes', methods=['GET'])
def getQuotes():
  
    topics = request.args.getlist('query')
    authors = request.args.getlist('author')
    # print(type(search))
    # print(search)
    data = get_quotes(topics)
    data2 = get_quotes_by_author(authors)
    quotes = []
    authors = []

    for quote in data:
        # print(quote.split('\n'))
        split_text = quote.split('\n')
        quotes.append(split_text[0])
        authors.append(split_text[-1])

    for quote in data2:
      # print(quote.split('\n'))
      split_text = quote.split('\n')
      quotes.append(split_text[0])
      authors.append(split_text[-1])
    
    return jsonify([quotes, authors, len(quotes)]), 200

if __name__ == "__main__":
  app.run()