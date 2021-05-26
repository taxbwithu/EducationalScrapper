from settings import db_user, db_password
import pymongo
import urllib.parse
import traceback
import pandas as pd


class MongoToCSV:

    def getCsv(self):
        username = urllib.parse.quote_plus(db_user)
        password = urllib.parse.quote_plus(db_password)

        url = "mongodb+srv://dbUser:root@zpicluster.oyapv.mongodb.net/test".format(username,
                                                                                                        password)
        client = pymongo.MongoClient(url)
        db = client.db.movies

        try:
            movies = db.find({})
            df = pd.DataFrame(list(movies))
            del df['_id']
            df.to_csv('movies.csv', sep=',', encoding='utf-8', index=False)
        except:
            traceback.print_exc()
            print('an error occurred movies were not converted to db')
