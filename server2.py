'''
    Simple socket server using threads
''' 
import socket
import sys
from thread import *
 
HOST = ''   		# Symbolic name meaning all available interfaces
PORT = 8188 		# Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'


chosen =0
def clientthread(conn):
    						
    x=0
    conn.send('Welcome to the server.\n') 	#send only takes string
    for x in range(i-1):
        conn.sendall(a[x] + ' is connected \n') 
    y=0
    for y in range(i-1):
        a1[y].sendall('new connected client  '+str(new)) 

    conn.sendall ('enter the client you want to chat with : \n')
    chosen = conn.recv(1024)

    if chosen:   
	    arr[0]=conn
	    p=0
	    for p in xrange (total):
		if (a[p]==chosen):
			arr[1]=a1[p]
	    
	    while True:
		#receiving from client
		data = conn.recv(1024)
		reply=data
		if not data:
			break
		if conn == arr[0]:
			arr[1].send(reply)
		else:
			arr[0].send(reply)
			#came out of loop   
           
    conn.close()   
new=0   
total=0  
arr={}
a1=[]
i=0 
a=[]

while 1:
    #wait to accept a connection - blocking call
    conn, addr= s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    a.append(str(addr[1]))	
    new= addr[1]
    total+=1
    a1.append(conn)
    start_new_thread(clientthread ,(conn,))		
    i+=1
s.close()
