import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

CONNECTION_STRING = os.environ.get('connection_string')

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_default_database()
article_collection = db.get_collection('articles')

def get_article_links_by_publisher(publisher):
    links = article_collection.find({'publisher':publisher}, {'_id':False, 'link': True})
    links = set(link['link'] for link in links)
    return links

def save_articles(articles):
    if len(articles) == 0:
        return
    articles = [article.__dict__ for article in articles]
    article_collection.insert_many(articles)

def get_all_articles():
    articles = article_collection.find({},{'_id':False, '_v':False})
    return list(articles)
    

print(get_article_links_by_publisher("CNBC"))