from flask import Flask, jsonify
from article import Article
from scraper import scrape_articles

app = Flask(__name__)

@app.route("/")
def get_articles():
    scrape_articles()
    articles = Article.get_all()
    return jsonify(articles)

if __name__ == "__main__":
    app.run(host='localhost',port=8080,debug=True)