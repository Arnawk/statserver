import glob
import sys
import numpy as np
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('./build/lib*')[0])

import logging
logging.basicConfig(level=logging.DEBUG)

import time
import random

from StatServer import *
from StatServer.ttypes import *

#from shared.ttypes import SharedStruct

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class StatServerHandler:
    def __init__(self):
        self.log = {}
    def ping(self):
        return True;
    def generateNums(self):
        #self.send_response(200)
        #self.send_header('Content-type', 'text/html')
        #self.end_headers()
        listOfNumbers=list(range(10))
        for i in range(0,9):
            random_number = random.randint(1, 4)
            if (random_number==3):
                random_ToAdd = random.randrange(1,10,2)
            else:
                random_ToAdd = random.randrange(0,11,2)
            listOfNumbers[i]=random_ToAdd
        return listOfNumbers
    def calculateStat(self, allNumbers):
        stSt = StatStruct()
        stSt.mean = np.mean(allNumbers);
        stSt.median = np.median(allNumbers);
        stSt.variance = np.var(allNumbers);
        stSt.stddev = np.std(allNumbers);
        
        return stSt;


if __name__ == '__main__':
    handler = StatServerHandler()
    processor = StatServer.Processor(handler)
    transport = TSocket.TServerSocket(host='0.0.0.0', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(
    #     processor, transport, tfactory, pfactory)

    server.serve()
