from tkinter import *
from tkinter import ttk
from mlsocket import MLSocket
import cv2
import socket
import sys
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
    if (pref_rence.get()==("-1")):
        
        HOST = ip_entry.get()
        PORT = int(port_entry.get())

        with MLSocket() as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, address = s.accept()

            with conn:
                while True:
                    data = conn.recv(1024) # This will block until it receives all the data send by the client, with the step size of 1024 bytes.
                    cv2.imshow('Input', data)

                    c = cv2.waitKey(1)
                    if c == 27: # ESC
                        s.close()
                        break
    else:
        
        # create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket to a specific address and port
        server_address = (ip_entry.get(), int(port_entry.get()))
        sock.bind(server_address)

        # listen for incoming connections
        sock.listen(5)
        def send(conn, message):
            send_str(conn, message)

        def receive(conn):
            while True:
                data = conn.recv(1024)
                if data:
                    get_input(sock,data)

        while True:
            # wait for a connection
            print('waiting for a connection')
            connection, client_address = sock.accept()

            try:
                print('connection from', client_address)

                receive_thread = threading.Thread(target=receive, args=(connection,))
                receive_thread.start()

                # read user input and send to the client
                while True:
                    message = input("Enter a message to send: ")
                    if not message:
                        break
                    send(connection, message)
                
            except Exception as e:
                    print(e)

            finally:
                # clean up the connection
                connection.close()




btn = ttk.Button(window, text="Submit", command=clicked)
btn.grid(row=2, column=0, columnspan=2)

window.mainloop()