from flask import Flask, jsonify
from article import Article
from scraper import CNBC, CBS
from datetime import datetime, timezone

def scrape_articles():
    # scrapers = [CNBC("CNBC","https://www.cnbc.com/"), CBSNews("CBS", "https://www.cbsnews.com")]
    scrapers = [CNBC("https://www.cnbc.com/")]

    articles_publish_time = Article.get_last_insert_time()
    if articles_publish_time is not None:
        time_elapsed_last_insert = datetime.now(timezone.utc) - articles_publish_time
        time_elapsed_last_insert = time_elapsed_last_insert.total_seconds() / 3600
        if time_elapsed_last_insert < 6:
            # Scrape articles once every 6 hours
            # Subject to change
            return

    for scraper in scrapers:
        
        # Scrape articles that have not been scraped already
        saved_links = Article.get_links_by_publisher(scraper.publisher)
        links = scraper.get_links()
        links = [link for link in links if link not in saved_links]

        articles = []
        for link in links:
            try:
                articles.append(scraper.parse_link(link))
            except Exception as e:
                print("Could not parse link: ",link)
                print(e)

        Article.save(articles)

app = Flask(__name__)

@app.route("/")
def get_articles():
    scrape_articles()
    articles = Article.get_all()
    return jsonify(articles)

if __name__ == "__main__":
    app.run(host='localhost',port=8080,debug=True)