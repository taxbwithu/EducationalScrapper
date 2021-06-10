from Extractor import *
from MongoToCSV import MongoToCSV
from HadoopHelper import HadoopHelper
import os
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
    
    hh.mapreduce("mapper.py", "reducer.py", "csvs/", "outputfolder/")
    hh.downloadFileFromHdfs('outputfolder/', "./")
    hh.rm("outputfolder/")
    
    hh.mapreduce("mapper.py", "reducedecades.py", "csvs/", "decadesOutput/")
    hh.downloadFileFromHdfs('decadesOutput/', "./")
    hh.rm("decadesOutput/")

    # jakies inne mapreduce

    hh.rm('csvs/'+filename)

    # obliczanie statystyk

    # os.removedirs("outputfolder/")
    # os.removedirs("decadesOutput/")
    
    # os.remove(filename)
    # print(rawData)