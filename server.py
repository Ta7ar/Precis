from flask import Flask, jsonify
import json
from webscraping import scraper

app = Flask(__name__)

@app.route("/")
def get_articles():
    articles = scraper.run()
    articles_json = [json.dumps(article.__dict__) for article in articles]
    return jsonify(articles_json)

if __name__ == "__main__":
    app.run(host='localhost',port=8080,debug=True)