import cv2
import socket
import numpy as np

HOST = 'localhost'
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print(f"Connected to server {HOST}:{PORT}")

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    raise IOError("Cannot access the webcam!")

while True:
    ret, frame = capture.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    #print(frame.tobytes().__sizeof__())
    #print(frame.shape)
    frame_bytes = frame.tobytes()
    back_to_matrix = np.frombuffer(frame_bytes, dtype=np.uint8)
    back_to_matrix.reshape(144, 176, 3)
    #print(back_to_matrix.shape)
    #cv2.imshow('Input', back_to_matrix)
    
    client_socket.send(frame_bytes)

    c = cv2.waitKey(1)
    if c == 27: # ESC
        client_socket.close()
        break



capture.release()
cv2.destroyAllWindows()