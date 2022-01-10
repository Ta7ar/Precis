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

print(get_article_links_by_publisher("CNBC"))