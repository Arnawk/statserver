import glob
import sys
sys.path.append('gen-py')
#sys.path.append('build/lib.linux-x86_64-2.7')
sys.path.insert(0, glob.glob('./build/lib*')[0])

from StatServer import *
from StatServer.ttypes import *


from thrift.transport import TSocket
from thrift.transport import TTransport
#from thrift.protocol import *
from thrift.protocol import TBinaryProtocol, TJSONProtocol
from thrift.server import TServer, THttpServer
#from http.server import BaseHTTPRequestHandler, HTTPServer


import time
import random

class StatServerHandler:
#    def do_OPTIONS(self):
#        self.send_response(200, "ok")
#        self.send_header('Access-Control-Allow-Origin', '*')
#        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
#        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
#        self.send_header("Access-Control-Allow-Headers", "Content-Type")
#        self.end_headers()

#    def do_GET(self):
#        self.send_response(200, "ok")
#        self.send_header('Access-Control-Allow-Origin', '*')
#        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
#        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
#        self.send_header("Access-Control-Allow-Headers", "Content-Type")
#        self.end_headers()
#
#        self.processRequest()
    def __init__(self):
        self.log = {}

    
    def ping(self):
        return True;
    def generateNums(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        listOfNumbers=[]
        for i in range(1,11):
            random_number = random.randint(1, 4)
            if (random_number==3):
                random_ToAdd = random.randrange(1,10,2)
            else:
                random_ToAdd = random.randrange(0,11,2)
            listOfNumbers[i]=random_ToAdd
        return listOfNumbers
        
    def calculateStat(self, allNumbers):
        return 5

if __name__ == '__main__':
    handler = StatServerHandler()
    processor = StatServer.Processor(handler)

   # tfactory = TTransport.TBufferedTransportFactory()
   # pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    # List of all protocols : https://thrift-tutorial.readthedocs.io/en/latest/thrift-stack.html

    #server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    #server = THttpServer.THttpServer(processor, ('0.0.0.0', 9090), pfactory)
    #transport = TSocket.TServerSocket(host='0.0.0.0', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TJSONProtocol.TJSONProtocolFactory()
    server = THttpServer.THttpServer(processor, ('',9090), pfactory)
#    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    

    print(time.asctime(), "Server Starts - :9090")
    try:
        server.serve()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print(time.asctime(), "Server Stops - :9090")
