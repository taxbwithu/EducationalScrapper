from Extractor import *
from MongoToCSV import MongoToCSV
# from Sender import *

if __name__ == '__main__':

    extractor = Extractor()
    # sender = Sender()
    csv_maker = MongoToCSV()

    # rawData = extractor.get_site()
    # sender.sendData(rawData)
    csv_maker.getCsv()

    # print(rawData)