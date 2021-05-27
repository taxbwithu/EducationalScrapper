import os

class HadoopHelper:
    def mkdir(self, path):
        os.system(f"hdfs dfs -mkdir {path}")

    def rm(self, path):
        os.system(f"hdfs dfs -rm {path}")
        
    def addFileToHdfs(self, filename, hdfsPath):
        os.system(f"hdfs dfs -put ./{filename} {hdfsPath}")

    def downloadFileFromHdfs(self, hdfsPath, localPath):
        os.system(f"hdfs dfs -get {hdfsPath} {localPath}")

    def mapreduce(self, mapper = "mapper.py", reducer = "reducer.py", inputfolder="/csvs/", outputfile="/outputfile"):
        os.system(f'mapred streaming -files ./{mapper},./{reducer} -mapper {mapper} -reducer {reducer} -input {inputfolder} -output {outputfile}')

