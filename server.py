'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5188  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'
arr=[]
i=0
# Start listening on socket
s.listen(2)
print 'Socket now listening'
conn={}
addr={}

# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n')  # send only takes string
   
    # infinite loop so that function do not terminate and thread do not end.
    while True:

        # Receiving from client
        data = conn[1].recv(1024)
        while data:
            data=conn.recv(1024)
            reply=data 
            if not data: break
            if conn==arr[0]:
                arr[1].sendall(reply)
            else:
                arr[0].sendall(reply)
    # came out of loop
    conn.close()
    
# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    arr.append(conn)
    print 'Connected with '
    
    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn,))

s.close()
