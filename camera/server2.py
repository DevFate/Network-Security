from mlsocket import MLSocket
import cv2

HOST = 'localhost'
PORT = 8000

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
