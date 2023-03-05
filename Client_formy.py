from tkinter import *
from tkinter import ttk
import cv2
import socket
import numpy as np
import time
import cv2
import socket
import numpy as np
from mlsocket import MLSocket
import time
import socket
import threading
from helpers import send_str, get_input, decode_bytes




window = Tk()
window.title("Welcome to TutorialsPoint")
window.geometry('400x400')
window.configure(background="grey")
a = Label(window, text="IP Address").grid(row=0, column=0)
b = Label(window, text="PORT").grid(row=1, column=0)
c = Label(window ,text = "pref").grid(row = 2,column = 0)
ip_entry = Entry(window)
ip_entry.grid(row=0, column=1)
port_entry = Entry(window)
port_entry.grid(row=1, column=1)
pref_rence = Entry(window)
pref_rence.grid(row = 2,column = 1)

def clicked():
    if(pref_rence.get() == ("-1")):
        HOST = ip_entry.get()
        PORT = int(port_entry.get())

        with MLSocket() as s:
            s.connect((HOST, PORT))
            print(f"Connected to server {HOST}:{PORT}")

            capture = cv2.VideoCapture(0)

            if not capture.isOpened():
                raise IOError("Cannot access the webcam!")

            while True:
                ret, frame = capture.read()
                s.send(frame)
                time.sleep(0.1)


                c = cv2.waitKey(1)
                if c == 27: # ESC
                    s.close()
                    break

            capture.release()
            cv2.destroyAllWindows()
    else:
        
        Is_connected = False
        host_ip = ip_entry.get()
        server_port = int(port_entry.get())


        def function(host_ip,server_port,Is_conected = False):
            while True:    
                try:
                    global tcp_client 
                    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    tcp_client.connect((host_ip, server_port))
                    Is_connected = True
                    return Is_connected
                except:
                    Is_connected = False
                    print("Failed to connect to server.")
                    continue


        connection = function(host_ip,server_port,Is_connected)
        def send(tcp_client, host_ip,server_port):
            try:
                while True:
                    data = input("")
                    #uses the helper function to encrypt and send the data
                    send_str(tcp_client,data)
                    
                #
            except socket.error as error:
                    print("Failed to send data to server.")
                    function(host_ip,server_port)
                #received = tcp_client.recv(1024)
                
                
                
                #print("Bytes Received: {}".format(received.decode()))
                #connection = function(host_ip,server_port,Is_connected)
                #if (connection == False):
                #    break
        def recieve(tcp_client):
            msg = tcp_client.recv(1024)
            try:
                while msg:
                    get_input(tcp_client, msg)
                    msg = tcp_client.recv(1024)
            except socket.error as error:
                    print("Failed to send data to server.")
                    function(host_ip,server_port)

        threading.Thread(target=send, args=(tcp_client, host_ip,server_port)).start()
        threading.Thread(target=recieve, args=(tcp_client,)).start()

btn = ttk.Button(window, text="Submit", command=clicked)
btn.grid(row=2, column=0, columnspan=2)

window.mainloop()
