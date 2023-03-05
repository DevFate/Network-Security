import socket
import sys
import threading

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('192.168.137.108', 8000)
sock.bind(server_address)

# listen for incoming connections
sock.listen(1)
def send(conn, message):
    conn.sendall(message.encode())

def receive(conn):
    while True:
        data = conn.recv(1024)
        if data:
            print("Received: {}".format(data.decode()))

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

    finally:
        # clean up the connection
        connection.close()
