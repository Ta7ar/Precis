from flask import Flask, jsonify, request, abort, Response
import article
import scraper

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    scraper.scrape_articles()
    articles = article.get_all()
    return jsonify(articles)

@app.route("/api",methods=['GET'])
def get_articles_paginated():
    limit, offset = request.args.get('limit', 10), request.args.get('offset', 0)
    limit, offset = int(limit), int(offset)
    data = article.get(limit,offset)
    if data is None:
        abort(Response('Offset value exceeds total number of articles available.', 404))     
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='localhost',port=8080,debug=True)