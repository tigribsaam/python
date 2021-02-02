import socket               # Import socket module
from time import sleep

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

while True:
    try:
        s.connect((host, port))
        response = s.recv(1024).decode("utf-8")
        print(response)
        s.close()
        if response:
            break
    except Exception as e:
        sleep(4)
        print(e)
