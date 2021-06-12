from Extractor import *
from MongoToCSV import MongoToCSV
from HadoopHelper import HadoopHelper
import os
from makecharts import makeCharts
# from Sender import *

filename = 'movies.csv'

if __name__ == '__main__':

    extractor = Extractor()
    # sender = Sender()
    csv_maker = MongoToCSV()
    # rawData = extractor.get_site()
    # sender.sendData(rawData)
    csv_maker.getCsv()
    print('utworzenie hh')
    hh = HadoopHelper()
    print('wysylanie')
    hh.addFileToHdfs(filename, 'csvs/'+filename)
    print('odpalanie mapreduce')
    names = []

    name = 'mr/'
    hh.mapreduce("mapper.py", "reducer.py", "csvs/", name)
    hh.downloadFileFromHdfs(name, "./")
    hh.rm(name)
    names.append(name)
    
    name = 'mrd/'
    hh.mapreduce("mapper.py", "reducedecades.py", "csvs/", name)
    hh.downloadFileFromHdfs(name, "./")
    hh.rm(name)

    name = 'dec_mean/'
    hh.mapreduce("map_dec_mean.py", "red_dec_mean.py", "csvs/", name)
    hh.downloadFileFromHdfs(name, "./")
    hh.rm(name)
    names.append(name)

    # jakies inne mapreduce

    hh.rm('csvs/'+filename)

    # obliczanie statystyk
    makeCharts()

    for name in names:
        os.removedirs(name)
    
    # os.remove(filename)
    # print(rawData)