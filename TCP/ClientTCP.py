from socket import *
from datetime import *
from subprocess import *
server_name = 'localhost'
server_port = 50007

soc = socket(AF_INET, SOCK_STREAM)
soc.connect((server_name, server_port))

try:
    start_time = datetime.now()
    soc.send("get_time".encode())
    response = soc.recv(4096)
    end_time = datetime.now()

    offset = end_time - start_time

    print(response.decode())
finally:
    soc.close()
