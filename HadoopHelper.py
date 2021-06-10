import os

class HadoopHelper:
    def mkdir(self, path):
        os.system("hdfs dfs -mkdir {}".format(path))

    def rm(self, path):
        os.system("hdfs dfs -rm -r {}".format(path))
        
    def addFileToHdfs(self, filename, hdfsPath):
        os.system("hdfs dfs -put ./{} {}".format(filename, hdfsPath))

    def downloadFileFromHdfs(self, hdfsPath, localPath):
        os.system("hdfs dfs -get {} {}".format(hdfsPath, localPath))

    def mapreduce(self, mapper = "mapper.py", reducer = "reducer.py", inputfolder="csvs/", outputfolder="/outputfile"):
        os.system('mapred streaming -files ./'+mapper+',./'+reducer+' -mapper "python3 '+mapper+'" -reducer "python3 '+reducer+'" -input '+inputfolder+' -output '+outputfolder)