import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

CONNECTION_STRING = os.environ.get('connection_string')

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_default_database()
article_collection = db.get_collection('articles')
print(db.list_collection_names())