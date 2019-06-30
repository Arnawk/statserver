#!/usr/bin/python2.7

import sys
sys.path.append('./gen-py')
from StatServer import *
from StatServer.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import time
import random
#import statistics
hostName = "0.0.0.0"
hostPort = 9090

class StatServerHandler:
    def __init__(self):
        self.log={}
    def ping(self):
        res=True
        return res


if __name__ == '__main__':
    handler = StatServerHandler()

    processor = StatServer.Processor(handler)
    transport = TSocket.TServerSocket(host=hostName,port=hostPort)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# set server
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    #server.serve()
    print('Starting server')
    server.serve()
