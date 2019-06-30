#!/usr/bin/python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import random
import statistics

hostName = ""
hostPort = 9090

class MyServer(BaseHTTPRequestHandler):

	#	GET is for clients geting the predi
	def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if '/CALCULATE-STATS' in self.path:
                    pos = self.path.find('?')
                    allNumbers = self.path[pos+1:]
                    listOfNumbers = allNumbers.split(',');
                    for i in range(0, len(listOfNumbers)):
                        listOfNumbers[i] = int(listOfNumbers[i])
                    
                    mean = str(statistics.mean(listOfNumbers))
                    median = str(int(statistics.median(listOfNumbers)))
                    variance = str(statistics.variance(listOfNumbers))
                    stddev = str(statistics.stdev(listOfNumbers))
                    
                    res = "mean:"+mean+",median:"+median+",variance:"+variance+",std-dev:"+stddev
                    self.wfile.write(bytes(res, "utf-8"))
            else:
                if '/GEN-RAND' in self.path:
                    res=""
                    for i in range(1,11):
                        random_number = random.randint(1, 4)
                        if (random_number==3):
                            random_ToAdd = random.randrange(1,10,2)
                        else:
                            random_ToAdd = random.randrange(0,11,2)
                        if(i==10):
                            res = res + str(random_ToAdd)
                        else:
                            res = res + str(random_ToAdd) + ","
                    self.wfile.write(bytes(res, "utf-8"))
                else:
                    self.wfile.write(bytes("Route does not exist", "utf-8"))

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
