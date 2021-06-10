from settings import db_user, db_password
import pymongo
import traceback
from urllib.parse import urlparse

class Sender:
    def sendData(self, raw_data):
        string_data = ([movie.__dict__ for movie in raw_data])
        username = ''
        password = ''
        
        try:
            username = urlparse.quote_plus(db_user)
            password = urlparse.quote_plus(db_password)
        except AttributeError:
            username = db_user
            password = db_password
        url = "mongodb+srv://{}:{}@zpicluster.oyapv.mongodb.net/zpi?retryWrites=true&w=majority".format(username, password)
        client = pymongo.MongoClient(url)
        db = client.db.movies
        db.remove({})
        try:
            db.insert_many(string_data)
            print('inserted movies')
        except:
            traceback.print_exc()
            print('an error occurred movies were not stored to db')