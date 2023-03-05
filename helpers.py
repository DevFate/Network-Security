from configparser import ConfigParser
from encryptions.monke import encrypt, decrypt

# obtain the 3 keys used for the encryption of network traffic
parser = ConfigParser()
parser.read('configs.conf')
KEY1 = parser['security']['KEY1']
KEY2 = parser['security']['KEY2']
KEY3 = parser['security']['KEY3']

def send_str(conn_socket: object, string: str) -> None:
    encrypted_string = encrypt(string, KEY1, KEY2, KEY3) # ENCRYPTS STRING BEFORE SENDING IT TO THE CLIENT
    conn_socket.sendall(encrypted_string.encode('utf-8'))

def get_input(conn_socket: object, prompt: str, buffer_size: int = 1024) -> str:
    send_str(conn_socket, prompt)
    input_ = conn_socket.recv(buffer_size)
    input_ = decode_bytes(input_)
    decrypted_message, checksum_valid = decrypt(input_, KEY1, KEY2, KEY3)
    if not checksum_valid:
        print("[!] Checksum received by client is INVALID! This could mean that the data sent from the client was tampered-with!")
        print("[!] Potentially tampered-with data received:", decrypted_message)
        return None
    else: # CHECKSUM IS VALID
        return decrypted_message


def decode_bytes(bytes_: bytes) -> str:
    return bytes_.decode('utf-8').replace('\n', '')
