import socket
import threading


Is_connected = False
host_ip = input("Please type in the server IP address:\n").strip()
while (host_ip != "localhost" and host_ip.count('.') != 3):
    host_ip = input("Please type in a valid IP address:\n").strip()

server_port = -1

try:
    server_port = int(input("Please type in the port of the server:\n").strip())
except ValueError:
    while (True):
        try:
            server_port = int(input("Please type in a valid port:\n").strip())
            if server_port > 0 and server_port < 65535:
                break
            else:
                continue
        except:
            continue


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

            tcp_client.sendall(data.encode())
            ("Bytes Sent:     {}".format(data))
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
            print("Bytes Received: {}".format(msg.decode()))
            msg = tcp_client.recv(1024)
    except socket.error as error:
            print("Failed to send data to server.")
            function(host_ip,server_port)

threading.Thread(target=send, args=(tcp_client, host_ip,server_port)).start()
threading.Thread(target=recieve, args=(tcp_client,)).start()