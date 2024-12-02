import os

import mongoengine as db


def init_db():
    db.connect(
        db=os.getenv("MONGO_DB"),
        username=os.getenv("MONGO_USER"),
        password=os.getenv("MONGO_PASSWORD"),
        host=os.getenv("MONGO_URI"),
        authentication_source='admin'
    )
