import pymongo
from dotenv import load_dotenv
import os
from datetime import timezone
from typing import List
import summarizer

load_dotenv()

CONNECTION_STRING = os.environ.get('connection_string')

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_default_database()
article_collection = db.get_collection('articles')

class Article:
    def __init__(self,title,body,publisher,link) -> None:
        self.title = title
        self.body = summarizer.summarize(body)
        self.publisher = publisher
        self.link = link
    
    def __repr__(self) -> str:
        return f'''
        {self.title} | {self.publisher}

        {self.body}

        Read more here: {self.link}
        '''

def get_links_by_publisher(publisher):
    links = article_collection.find({'publisher':publisher}, {'_id':False, 'link': True})
    links = set(link['link'] for link in links)
    return links

def save(articles: List['Article']):
    if len(articles) == 0:
        return
    articles = [article.__dict__ for article in articles]
    article_collection.insert_many(articles)

def count_docs():
    return article_collection.count_documents({})

def get(limit, offset):
    starting_id = article_collection.find().sort('_id', pymongo.ASCENDING)[offset]['_id']
    articles = article_collection.find({'_id': {'$gte': starting_id}}, {'_id': False}).sort('_id', pymongo.ASCENDING).limit(limit)
    return list(articles)

    
def get_last_insert_et_and_date(current_datetime):
    record = article_collection.find_one({},sort=[('_id', pymongo.DESCENDING)])
    if record is None:
        return None, None

    last_insert_time = record.get('_id').generation_time
    last_insert_time.replace(tzinfo=timezone.utc)

    elapsed_time = current_datetime - last_insert_time
    elapsed_time = elapsed_time.total_seconds() / 3600

    last_insert_date = last_insert_time.date()

    return elapsed_time, last_insert_date

def delete_all():
    article_collection.delete_many({})
