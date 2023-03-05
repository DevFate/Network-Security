import socket
import sys
import threading
from helpers import send_str, get_input, decode_bytes

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('172.20.10.11', 8000)
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
