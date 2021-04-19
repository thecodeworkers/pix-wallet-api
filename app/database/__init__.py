from pymongo import MongoClient
from bson import json_util
from .skeleton import databases
from ..config.constant import DATABASE_HOST, DATABASE_PORT
from ..console.colors import OKGREEN, ENDC
import re
import json

class MigrateDatabase():
    def __init__(self):
        self.__client = None
        self.__init_connection()
        self.__migrate()

    def __init_connection(self):
        self.__client = MongoClient(DATABASE_HOST, DATABASE_PORT)

    def __read_documents(self, collection_name):
        with open(f'app/database/collections/{collection_name}') as f:
            bsondata = f.read()

            jsondata = re.sub(r'ObjectId\s*\(\s*\"(\S+)\"\s*\)',
                            r'{"$oid": "\1"}',
                            bsondata)
            jsondata = re.sub(r'ISODate\s*\(\s*(\S+)\s*\)',
                            r'{"$date": \1}',
                            jsondata)
            jsondata = re.sub(r'NumberInt\s*\(\s*(\S+)\s*\)',
                            r'{"$numberInt": "\1"}',
                            jsondata)

            file_data = json.loads(jsondata, object_hook=json_util.object_hook)

        return file_data

    def __migrate(self):
        try:
            for database in databases:
                db_name = database['name']
                db_collections = database['collections']

                db = self.__client[db_name]

                for db_collection in db_collections:
                    collection_name = db_collection.split('.')[0]
                    collection = db[collection_name]

                    if not collection.count_documents({}):
                        data = self.__read_documents(db_collection)
                        collection.insert_many(data)

            print(f'{OKGREEN} Database migrate successfully{ENDC}')
            self.__client.close()

        except Exception as error:
            self.__client.close()
            raise Exception(error)