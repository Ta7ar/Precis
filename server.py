from flask import Flask, jsonify
from article import Article
import scraper

app = Flask(__name__)

@app.route("/")
def get_articles():
    scraper.scrape_articles()
    articles = Article.get_all()
    return jsonify(articles)

if __name__ == "__main__":
    app.run(host='localhost',port=8080,debug=True)