from flask import Flask, jsonify, request, abort, Response, render_template
import article
import scraper

app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

@app.route("/api",methods=['GET'])
def get_articles_paginated():
    limit, offset = request.args.get('limit', 5), request.args.get('offset', 0)
    limit, offset = int(limit), int(offset)
    if offset == 0:
        scraper.scrape_articles()
    data = article.get(limit,offset)
    if data is None:
        abort(Response('Offset value exceeds total number of articles available.', 404))     
    return jsonify(data)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost',port=8080,debug=True)