from Extractor import *
from Wrapper import *
from Sender import *

if __name__ == '__main__':

    extractor = Extractor()
    wrapper = Wrapper()
    sender = Sender()

    rawData = extractor.getSite()
    dataModel = wrapper.packData()


    print(rawData)