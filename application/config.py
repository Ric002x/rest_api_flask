import os

import mongoengine as db
import mongomock
from dotenv import load_dotenv

load_dotenv()


def init_db():
    db.connect(
        db=os.getenv("MONGO_DB"),
        username=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
        host=os.getenv("MONGO_URI"),
        authentication_source='admin'
    )


def init_db_prod():
    db.connect(
        db=os.getenv("MONGO_DB"),
        host=os.getenv("MONGODB_URI")
    )
    print("Connected to the Mongo Atlas")
    print(os.getenv("MONGODB_URI"))


def init_db_tests():
    db.connect('mongoenginetest', host='mongodb://localhost',
               mongo_client_class=mongomock.MongoClient)
