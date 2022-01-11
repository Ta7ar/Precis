from flask import Flask, jsonify
import json
from webscraping import scraper
from db import get_all_articles

app = Flask(__name__)

@app.route("/")
def get_articles():
    '''
    Steps:
    1. Check dates of articles. If not current date, delete.
    2. Scrape article links.
    3. Scrape article if link does not exist in db and then save article in db
    4. Get all articles from db
    '''
    scraper.run()
    articles = get_all_articles()
    return jsonify(articles)

if __name__ == "__main__":
    app.run(host='localhost',port=8080,debug=True)