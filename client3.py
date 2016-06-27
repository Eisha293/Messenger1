import  socket 
import sys
from thread import *
from Tkinter import*
import random
global m
global data1
data1=''
m=40
host =''
port = 8916
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect((host, port))

def callback(event,data):

    print "clicked at",data, " ", event.x,event.y

def text_place_handler(self,text_place):
	  	
	global m
	p=text_place.get('1.0',"end-1c")
 
        text_place.delete('1.0',"end-1c")
	send = ''
	send=">>"+p
	w= Message(root,text=send,width=100)
	w.place(x=150, y=m, width=120, height=25)
	w.config(bg="red",font=('times',12,'italic'))
        print p
	m=m+35
        #print "clicked at", event.x, event.y
        s.sendall(p)
	
	
def call1(data):
	button = Button (root,text=str(data),width=5,height=1, fg="red")
	button.place(x=150,y=0,width=350,height=30)
	data1=data
	s.send(data1)
	

def create_client_module(parent):
	def recv():
		i=0
		global m
    		while True:
			data=''
			data = s.recv(5)
			if not data:
				sys.exit(0)
			print data
			if data.isdigit():			
				ct=[random.randrange(256) for x in range(3)]
				brightness=int(round(0.299*ct[0]+0.587*ct[1]+0.114*ct[2]))
				ct_hex="%02x%02x%02x" % tuple(ct)
				bg_colour='#'+"".join(ct_hex)	
				button=Button(parent, text=str(data),width=7 ,command=lambda:call1(data), height=1, fg="red", bg=bg_colour)
				button.place(x=20,y=30+i*30,width=120,height=25)
				i=i+1
			else:
				w= Message(parent,text=data,width=100)
				w.place(x=150, y=m, width=120, height=25)
				w.config(bg="red",font=('times',12,'italic'))
				print data
				m=m+35
	start_new_thread(recv ,())

class DrawBottomFrame:

    def __init__(self,root):

        fm=Frame(root,bg="green")
        fm.place(x=150,y=350,width=350,height=150)
        text_place=Text(fm,bg="white")
	
        text_place.place(x=5,y=5,width=340,height=140)
	send = Button (root,text="SEND",bg="black",fg="white",width= 7, font= ("Calibri",10,'bold'),height=3,command=lambda:text_place_handler(root,text_place))
	send.place(x=365,y=470,width=120,height=25)
		
root=Tk()
left_frame=Frame(root,bg="blue")
left_frame.place(x=0,y=0,width=150,height=500)
create_client_module(left_frame)

center_frame=Frame(root,bg="red")
center_frame.place(x=150,y=0,width=350,height=350)

bottom=DrawBottomFrame(root)
root.geometry('500x500')
root.resizable(width=False,height=False)
root.mainloop()



