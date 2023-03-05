import os
from helpers import send_str, get_input

def main(conn: object):
    local_file = get_input(conn, "Local file> ")
    remote_path = get_input(conn, "Remote path> ")
    
    with open(local_file, mode='rb') as file_to_upload:
        file_stream = file_to_upload.read()
        
