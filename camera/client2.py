import cv2
import socket
import numpy as np
from mlsocket import MLSocket
import time

HOST = '172.20.10.11'
PORT = 8000

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