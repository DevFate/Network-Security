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
    frame = cv2.resize(frame, (100, 100))
    frame_bytes = frame.tobytes()
    client_socket.send(frame_bytes)

    c = cv2.waitKey(1)
    if c == 27: # ESC
        client_socket.close()
        break



capture.release()
cv2.destroyAllWindows()