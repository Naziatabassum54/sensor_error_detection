from sensor.configration.mongo_db_connection import MongoDBClient

if __name__ == '__main__':
    mongodb_client = MongoDBClient()
    print("Collection name:",mongodb_client.database.list_collection_names())