from pymongo.database import Database as MongoDatabase
from pymongo import MongoClient

class MongoManager:
    client: MongoClient
    conn: MongoDatabase

    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name

        self.client = MongoClient(self.uri)
        self.conn = self.client[self.db_name]

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        # self.client.close()
        pass