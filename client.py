from socket import *   # Import socket module
from threading import Thread
impoort sys

s = socket(AF_INET,SOCK_STREAM)
host = 'localhost'
port = 5188  # Reserve a port for your service.

s.connect((host, port))
def recv ():
  while True:
    data=s.recv(1024)
    if not data:
      sys.exit(0)
    print data
Thread (target=recv).start()
while True:
  data= raw_input(' >> ')
  s.send(data)
  
s.close  # Close the socket when done
