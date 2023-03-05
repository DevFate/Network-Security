import socket
import cv2
import numpy as np

# Define the host and port to listen on
HOST = 'localhost'
PORT = 8000

BUFFER = 76032

# Create a TCP socket and bind it to the host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# Wait for a client to connect
client_socket, client_address = server_socket.accept()

print(f"Client connected from {client_address[0]}:{client_address[1]}")

# Receive data from the client
while True:
    data = client_socket.recv(BUFFER)
    if not data:
        print("STOPPING")
        break
    
    frame = np.frombuffer(data, dtype=np.uint8)
    frame = frame.reshape(144, 176, 3)

    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27: # ESC
        client_socket.close()
        break


# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
