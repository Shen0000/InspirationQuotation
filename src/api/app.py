from flask import Flask, request
import json
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../scripts')

from quotes import *

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/get-quotes', methods=['GET'])
def getQuotes():
    search = request.args.getlist('querry')
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