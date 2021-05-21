from settings import db_user, db_password
import pymongo
import urllib.parse
import traceback

class Sender:

    def sendData(self, raw_data):
        string_data = ([movie.__dict__ for movie in raw_data])

        username = urllib.parse.quote_plus(db_user)
        password = urllib.parse.quote_plus(db_password)

        url = "mongodb+srv://{}:{}@zpicluster.oyapv.mongodb.net/zpi?retryWrites=true&w=majority".format(username, password)
        client = pymongo.MongoClient(url)
        db = client.db.movies

        try:
            db.insert_many(string_data)
            print(f'inserted {len(string_data)} movies')
        except:
            traceback.print_exc()
            print('an error occurred movies were not stored to db')