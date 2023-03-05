import socket
import threading
from helpers import send_str, get_input, decode_bytes

Is_connected = False
host_ip = 
server_port = 



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