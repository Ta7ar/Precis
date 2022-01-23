import math
from flask import Flask, jsonify, request, abort, Response, render_template
import article
import scraper

ARTICLES_LIMIT = 5

app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

@app.route("/api/<int:page>",methods=['GET'])
def get_articles_paginated(page):
    if page < 1:
        abort(Response('Page number must be a positive number.', 404))     
    if page == 1:
        scraper.scrape_articles()
    article_docs_count = article.count_docs()
    offset = (page-1)*ARTICLES_LIMIT
    if offset > article_docs_count:
        abort(Response('Page does not exist.', 404))
    articles = article.get(ARTICLES_LIMIT,offset)
    total_page_count = math.ceil(article_docs_count/ARTICLES_LIMIT)
    data = {
        'articles': articles,
        'pages': total_page_count
    }
    return jsonify(data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == "__main__":
    from waitress import serve
    import logging
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.INFO)
    serve(app,host='0.0.0.0',port=8080)